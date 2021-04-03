fn parse_sequences(path: String) -> Vec<String> {
    use std::fs::File;
    use std::io::{BufRead, BufReader};
    let f = BufReader::new(File::open(path).unwrap());
    let mut result: Vec<String> = Vec::new();
    let mut current = String::new();

    for l in f.lines() {
        match l {
            Ok(x) => {
                if x.trim().starts_with(">") {
                    if ! current.is_empty() {
                        result.push(current);
                        current = String::new();
                    }
                } else {
                    current.push_str(x.trim());
                }
            },
            _ => (),
            }
        }
    result.push(current);
    result
}

fn build_edit_distance_table(seq1: &String, seq2: &String) -> Vec<Vec<u64>> {
    use std::cmp::min;

    let mut result: Vec<Vec<u64>> = vec![ vec![0; seq2.len()+1]; seq1.len()+1];

    for i in 0..seq1.len()+1 {
        result[i as usize][0] = i as u64;
    }
    
    for i in 0..seq2.len()+1 {
        result[0][i as usize] = i as u64;
    }

    for (i1, c1) in seq1.chars().enumerate() {
        for (i2, c2) in seq2.chars().enumerate() {
            let mut delta: u64 = 1;
            if c1 == c2 {
                delta = 0;
            }
            let mini: u64 = min(
                                min(result[i1][i2]+delta, result[i1+1][i2]+1),
                                min(result[i1][i2]+delta, result[i1][i2+1]+1)
                                    );
            result[i1+1][i2+1] = mini;
        }
    }
    result
}

fn augmented_string_build(edt: &Vec<Vec<u64>>, str1: &String, str2: &String) -> (String, String) {
    let chars1: Vec<char> = str1.chars().collect();
    let chars2: Vec<char> = str2.chars().collect();
    let mut result1 = String::new();
    let mut result2 = String::new();
    let mut i: usize = chars1.len();
    let mut j: usize = chars2.len();

    while (i, j) != (0, 0) {
        if i == 0 {
            result1.push('-');
            result2.push(chars2[j-1]);
            j -= 1;
        } else if j == 0 {
            result1.push(chars1[i-1]);
            result2.push('-');
            i -= 1;
        } else if  (edt[i-1][j-1] <= edt[i][j-1]) &&
                   (edt[i-1][j-1] <= edt[i-1][j]) {
            result1.push(chars1[i-1]);
            result2.push(chars2[j-1]);
            i -= 1;
            j -= 1;
        } else if edt[i][j-1] <= edt[i-1][j] {
            result1.push('-');
            result2.push(chars2[j-1]);
            j -= 1;
        } else if edt[i-1][j] <= edt[i][j-1] {
            result1.push(chars1[i-1]);
            result2.push('-');
            i -= 1;
        }
    }
    let result1 = result1.chars().rev().collect();
    let result2 = result2.chars().rev().collect();
    (result1, result2)
}

fn main() {
    let sequences: Vec<String> = parse_sequences(String::from("rosalind_edta.txt"));
    let EDT: Vec<Vec<u64>> = build_edit_distance_table(&sequences[0], &sequences[1]);
    let (aug_1, aug_2): (String, String) = augmented_string_build(&EDT, &sequences[0], &sequences[1]);
    println!("{}", EDT[sequences[0].len() as usize][sequences[1].len() as usize]);
    println!("{}", aug_1);
    println!("{}", aug_2);
}
