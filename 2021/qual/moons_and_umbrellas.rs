use std::io::BufRead;

fn main() {
    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = move || it.next().unwrap().unwrap();

    let n: i32 = read_line().parse().unwrap();
    for case_no in 0..n {
        let line = read_line();
        let mut it = line.split_whitespace();
        let x: i32 = it.next().unwrap().parse().unwrap();
        let y: i32 = it.next().unwrap().parse().unwrap();
        let s = it.next().unwrap();
        assert!(it.next().is_none());

        let inf = 1_000_000_000;
        let mut costs = (0, 0);
        for ch in s.chars() {
            let c_cost = costs.0.min(costs.1 + y);
            let j_cost = costs.1.min(costs.0 + x);
            costs = match ch {
                'C' => (c_cost, inf),
                'J' => (inf, j_cost),
                '?' => (c_cost, j_cost),
                _ => panic!(),
            }
        }
        println!("Case #{}: {}", case_no + 1, costs.0.min(costs.1));
    }
}
