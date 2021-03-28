use std::io::BufRead;

fn main() {
    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = || it.next().unwrap().unwrap();

    let n: i32 = read_line().parse().unwrap();
    for case_no in 0..n {
        let len: usize = read_line().parse().unwrap();
        let line = read_line();
        let mut xs: Vec<i32> = line.split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        assert_eq!(xs.len(), len);

        let mut cost = 0;
        for i in 0..xs.len() - 1 {
            let min_idx = (i..xs.len()).min_by_key(|&idx| xs[idx]).unwrap();
            cost += min_idx + 1 - i;
            xs[i..min_idx + 1].reverse();
        }
        println!("Case #{}: {}", case_no + 1, cost);
    }
}
