/*
Find the sum of all the multiples of 3 or 5 below 1000. (fizzbuzz++)
*/

fn euler_1(max_num : isize) -> isize {
    (0..max_num).filter(|&x| x % 3 ==0 || x % 5 == 0).sum()
}

fn main() {
    println!("{}", euler_1(1000));
}