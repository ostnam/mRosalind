use std::fs::File;
use std::io::{BufReader, BufRead};
use std::collections::HashMap;

fn main() {
    let mut blosum: HashMap<(String, String), i8> = HashMap::new();

    let file = File::open("blosum62.txt").expect("error opening blosum");
    let mut buf_reader = BufReader::new(file);
    
    let lines = buf_reader.lines();
    let mut header_set: bool = false;
    let mut header: Vec<String> = Vec::new();
    for line in lines {
        let linestr = line.unwrap();
        if ! header_set {
            header_set = true;
            for c in linestr.trim().split("  ") {
                header.push(c[0..1].to_string());
            }
        } else {
            let l: Vec<&str> = linestr.split_whitespace().collect();
            let col = l[0];
            for (i, v) in l.iter().skip(1).enumerate() {
                blosum.entry( (header[i].clone(), col.to_string()) ).or_insert(v.parse::<i8>().unwrap());
            }
        }
    }
    println!("{:?}", header);
    println!("{:?}", blosum);
}
