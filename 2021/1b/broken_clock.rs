use std::io::BufRead;

const M: i128 = 360 * 12 * 10_000_000_000;

fn main() {
    let inv11 = (0..11).find_map(|i| {
        let t = 1 + i * M;
        if t % 11 == 0 { Some(t / 11) } else { None }
    }).unwrap();
    assert_eq!((11 * inv11) % M, 1);

    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = move || it.next().unwrap().unwrap();

    let line = read_line();
    let t: i32 = line.parse().unwrap();

    for case_no in 0..t {
        let line = read_line();
        let mut it = line.split_whitespace();
        let hand1: i128 = it.next().unwrap().parse().unwrap();
        let hand2: i128 = it.next().unwrap().parse().unwrap();
        let hand3: i128 = it.next().unwrap().parse().unwrap();
        assert!(it.next().is_none());

        let mut time = None;
        for &(hand_h, hand_m, hand_s) in &[
            (hand1, hand2, hand3),
            (hand1, hand3, hand2),
            (hand2, hand1, hand3),
            (hand2, hand3, hand1),
            (hand3, hand1, hand2),
            (hand3, hand2, hand1),
        ] {
            let t = (inv11 * (hand_m - hand_h + M)) % M;
            if (719 * t + hand_h) % M == hand_s {
                time = Some(t);
                break;
            }
        }
        let time = time.unwrap();

        let ns = time % 1_000_000_000;
        let time = time / 1_000_000_000;
        let s = time % 60;
        let time = time / 60;
        let m = time % 60;
        let time = time / 60;
        let h = time;

        println!("Case #{}: {} {} {} {}", case_no + 1, h, m, s, ns);
    }
}
