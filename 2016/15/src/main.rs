use std::fs;

#[derive(Copy, Clone)]
struct Disc {
    id: i32,
    positions: i32,
    start: i32,
}

fn parse_input(filename: &str) -> Vec<Disc> {
    let mut discs: Vec<Disc> = Vec::new();
    let read_lines = fs::read_to_string(filename).expect("Failed to open file");
    let lines = read_lines.split('\n').collect::<Vec<&str>>();
    let mut id_st = 1;

    for l in lines {
        let l_str = l.to_string();
        let l_str_split = l_str.split(' ').collect::<Vec<&str>>();
        let pos = l_str_split[3].to_string().parse::<i32>().unwrap();
        let start_string = l_str_split[11].to_string();
        let start_split = start_string.split('.').collect::<Vec<&str>>();
        let strt = start_split[0].to_string().parse::<i32>().unwrap();

        discs.push(Disc {
            id: id_st,
            positions: pos,
            start: strt,
        });
        id_st += 1;
    }

    discs
}

fn play_game(discs: &[Disc]) -> i32 {
    let mut time_to_press = 0;
    loop {
        let mut change = true;

        for disc in discs.iter() {
            if (disc.id + time_to_press + disc.start) % disc.positions != 0 {
                change = false;
                break;
            }
        }

        if change {
            return time_to_press;
        }
        time_to_press += 1;
    }
}

fn main() {
    let all_discs = parse_input("src/15.in");
    let mut all_discs_clone = all_discs.clone();
    all_discs_clone.push(Disc {
        id: 7,
        positions: 11,
        start: 0,
    });
    let mut time_to_press = play_game(&all_discs);
    // part 1
    println!("{}", time_to_press);
    time_to_press = play_game(&all_discs_clone);
    // part 2
    println!("{}", time_to_press);
}
