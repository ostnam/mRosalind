use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut f = BufReader::new(File::open("rosalind_ddeg.txt").unwrap());
    let mut l1 = String::new();
    f.read_line(&mut l1).unwrap();
    let n1: Vec<u16> = l1.split(char::is_whitespace)
                         .take(2)
                         .map(|x| x.parse::<u16>().unwrap())
                         .collect();
    // parse the 2 ints of the first line
    
    let mut graph: Vec<Vec<u16>> = Vec::with_capacity(n1[0] as usize);

    for _i in 0..n1[0] {
        graph.push(Vec::new());
    }

    for l in f.lines() {
        match l {
            Ok(x) => {
            let edges: Vec<u16> = x.split(char::is_whitespace)
                          .take(2)
                          .map(|x| x.parse::<u16>().unwrap())
                          .map(|x| x-1)
                          .collect();
            graph[edges[0] as usize].push(edges[1]);
            graph[edges[1] as usize].push(edges[0]);
            },
            _ => (),
        };
    }

    for i in &graph {
        let mut count: u32 = 0;
        for j in i {
            count += graph[*j as usize].len() as u32;
        }
        print!("{} ", count);
    }
    print!("\n");
}
