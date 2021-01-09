// my solution to the ins problem
//
// compile it with rustc ("rustc ins.rs")
// then run it with command expansion to replace the file to positional arguments :
// ./ins $(cat rosalind_ins.txt)

use std::env;
use std::convert::TryInto;
use std::convert::TryFrom;

fn main() {
    let args: Vec<String> = env::args().collect();
    let n: u32 = args[1].parse::<u32>().unwrap(); // n is the length of A and the first positional arguments when we pipe the problem file
    let mut a: Vec<i32> = Vec::new();
    let mut count: u32 = 0;
    for i in 2..2+n {
        let index = usize::try_from(i).unwrap();
        a.insert((i - 2).try_into().unwrap(), args[index].parse::<i32>().unwrap());
    }
    for i in 0..n {
        let mut k = i;
        while k > 0 && a[usize::try_from(k).unwrap()] < a[usize::try_from(k-1).unwrap()] {
            a.swap((k - 1).try_into().unwrap(), k.try_into().unwrap());
            k -= 1;
            count += 1;
        }
    }
    println!("{:?}", count);
}
