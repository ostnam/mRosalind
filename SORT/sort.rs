// run gen_permutations.py before running this
use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let mut permutations_array: [(usize, usize); 45] = [(0, 0); 45];
    let permutations_file = File::open("permutations.txt").unwrap();
    let mut array_index: usize = 0;

    for line in io::BufReader::new(permutations_file).lines() {
        match line {
            Ok(string) => {
                let digits:Vec<&str> = string.split_whitespace().collect();
                permutations_array[array_index] = (digits[0].parse::<usize>().unwrap(), digits[1].parse::<usize>().unwrap());
                array_index += 1;
            },
            _ => println!("error parsing permutations file"),
        }
    }
    
    let problem_file = File::open("rosalind_sort.txt").unwrap();
    let mut problem_arrays: Vec<String> = Vec::new();
    array_index = 0;
    for line in io::BufReader::new(problem_file).lines() {
        match line {
            Ok(string) => {
                let string = string.trim();
                let string = string.split_whitespace().map(|x| x.parse::<u8>().unwrap()).map(|x| x-1).map(|x| x.to_string()).collect::<String>(); 
                problem_arrays.push(string);
                array_index += 1;
            },
            _ => println!("error trying to parse rosalind_sort.txt"),
        }
    }

    struct Permutation {
        sequence: String,
        distance: u8,
        modifications: Vec<(usize, usize)>,
    }

    impl Permutation {
        fn permute(&self, new_mod: (usize, usize)) -> Permutation {
            let mut new_str = String::new();
            new_str.push_str(&self.sequence[0..new_mod.0]);
            new_str.push_str(&self.sequence[new_mod.0..new_mod.1].chars().rev().collect::<String>());
            new_str.push_str(&self.sequence[new_mod.1..]);

            let mut new_mod_vec = self.modifications.clone();
            new_mod_vec.push((new_mod.0+1, new_mod.1));
            let new_dist = self.distance + 1;

            return Permutation {
                sequence: new_str,
                distance: new_dist,
                modifications: new_mod_vec,
            };
        }
    }
    fn discordance(a: &str, b:&str, limit: u8) -> bool {
        let mut count = 0;
        for (i, j) in a.chars().zip(b.chars()) {
            if i != j {
                count += 1;
                if count == limit {
                    return false;
                }
            }
        }
        return true;
    }
    fn diff(a: &str, b:&str) -> u8 {
        let mut count = 0;
        for (i, j) in a.chars().zip(b.chars()) {
            if i != j {
                count += 1;
            }
        }
        return count;
    }
    let mut this_cycle: Vec<Permutation> = Vec::new();
    this_cycle.push(Permutation{
        sequence: problem_arrays[0].clone(),
        distance: 0,
        modifications: Vec::new(),
    });

    let mut sequences_seen_before: Vec<String> = Vec::new();
    let baseline = diff(&problem_arrays[0], &problem_arrays[1]);
    sequences_seen_before.push(problem_arrays[0].clone());

    for distance in 1..10 {
        let mut to_add: Vec<Permutation> = Vec::new();
        for i in &this_cycle {
                for j in &permutations_array {
                    let new = i.permute(*j);
                    if new.sequence == problem_arrays[1] {
                        println!("{}" , new.distance);
                        for i in &new.modifications {
                            println!("{} {}", i.0, i.1);
                        }
                        return;
                    }
                    if discordance(&new.sequence, &problem_arrays[1], baseline-distance+1) {
                        if ! sequences_seen_before.contains(&new.sequence) {
                            sequences_seen_before.push(new.sequence.to_string());
                            to_add.push(new);
                        }
                    }
                }
        }
        this_cycle = to_add;
    }
}
