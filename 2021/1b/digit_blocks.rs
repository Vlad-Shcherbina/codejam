use std::io::BufRead;

fn main() {
    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = move || it.next().unwrap().unwrap();

    let line = read_line();
    let mut it = line.split_whitespace();
    let t: i32 = it.next().unwrap().parse().unwrap();
    let n: usize = it.next().unwrap().parse().unwrap();
    let b: usize = it.next().unwrap().parse().unwrap();
    let _p: i64 = it.next().unwrap().parse().unwrap();

    for _case_no in 0..t {
        let mut heights = vec![0; n];
        let mut towers = vec![String::new(); n];
        for q in 0..n * b {
            let remaining = n * b - q;
            let d: i64 = read_line().parse().unwrap();

            let i = loop {
                if d == 9 {
                    let ii = (0..n).find(|&i| heights[i] + 1 == b);
                    if let Some(ii) = ii {
                        break ii;
                    }
                }
                if d >= 8 || remaining < 5 && d >= 5 {
                    let ii = (0..n).find(|&i| heights[i] + 2 == b);
                    if let Some(ii) = ii {
                        break ii;
                    }
                }
                let ii = (0..n).find(|&i| heights[i] + 2 < b);
                if let Some(ii) = ii {
                    break ii;
                }
                let ii = (0..n).find(|&i| heights[i] + 1 < b);
                if let Some(ii) = ii {
                    break ii;
                }
                break (0..n).find(|&i| heights[i] < b).unwrap();
            };

            heights[i] += 1;
            towers[i].push_str(&d.to_string());
            println!("{}", i + 1);
            if 0 < remaining && remaining < 10 {
                // dbg!(&towers[15..]);
            }
        }
        // dbg!(towers);
    }

    let verdict = read_line();
    dbg!(verdict);
}
