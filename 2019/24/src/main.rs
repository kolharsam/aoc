use std::fs::read_to_string;
// use std::collections::hash_set::HashSet; -- this is implemented as a hashmap where the value is ()

type Grid = Vec<Vec<bool>>;

/**
 * TIL: impl for a custom type / type alias
 * You'll have to first make a trait with all the functions
 * that you might use within your impl and
 * after that you can implement that trait
 * for your custom type.
 *
 * trait GridFns {
 *      fn print_grid(&self);
 *      fn get_alive_neighbours(&self, param1: i32) -> i32;
 * }
 *
 * impl GridFns for Grid {
 *      fn print_grid.....
 * }
*/

fn parse_file(filename: &str) -> Grid {
    let read_lines = read_to_string(filename).expect("Failed to open the file");
    let read_lines_split = read_lines.split('\n').collect::<Vec<&str>>();
    let mut init_grid: Vec<Vec<bool>> = Vec::new();

    for line in read_lines_split {
        let str_line = line.to_string();
        let str_line_split = str_line.split("").collect::<Vec<&str>>();
        let mut row: Vec<bool> = Vec::new();
        for s in str_line_split {
            if s == "." {
                row.push(false);
            } else if s == "#" {
                row.push(true);
            }
        }
        init_grid.push(row);
    }

    init_grid
}

fn play_game(init_state: &Grid) -> i32 {
    let current_state = init_state.to_owned();
    let mut loop_state = current_state.clone();
    let mut next_state = current_state.clone();
    let mut row = 0;
    let mut all_states: Vec<Vec<i32>> = Vec::new();

    let mut alive = get_alive(&current_state);
    all_states.push(alive);

    loop {
        while row < 5 {
            let mut col = 0;
            while col < 5 {
                let c = loop_state[row][col];
                let nc = get_neighbours(&loop_state, &row, &col);
                if nc == 1 || !c && nc == 2 {
                    next_state[row][col] = true;
                } else {
                    next_state[row][col] = false;
                }
                col += 1;
            }
            row += 1;
        }
        row = 0;
        alive = get_alive(&next_state);
        if all_states.contains(&alive) {
            print_grid(&next_state);
            println!("{:?}", alive);
            break;
        }
        all_states.push(alive);
        loop_state = next_state.clone();
    }

    get_biodiv_score(&alive)
}

fn get_neighbours(c_state: &Grid, c_row: &usize, c_col: &usize) -> i32 {
    let mut count = 0;

    if (*c_row as i32 + 1 < 5) && c_state[*c_row + 1][*c_col] {
        count += 1;
    }
    if (*c_col as i32 + 1 < 5) && c_state[*c_row][*c_col + 1] {
        count += 1;
    }
    if (*c_row as i32 - 1) >= 0 && c_state[*c_row - 1][*c_col] {
        count += 1;
    }
    if (*c_col as i32 - 1) as i32 >= 0 && c_state[*c_row][*c_col - 1] {
        count += 1;
    }

    count
}

fn get_alive(state: &Grid) -> Vec<i32> {
    let mut alive: Vec<i32> = Vec::new();
    let mut count = 0;
    for row in state {
        for val in row {
            if *val {
                alive.push(count);
            }
            count += 1;
        }
    }

    alive
}

fn get_biodiv_score(state: &[i32]) -> i32 {
    let current_state = state.to_owned();
    let mut sum = 0;
    let base: i32 = 2;
    current_state.iter().for_each(|x| sum += base.pow(*x as u32));

    sum
}

fn print_grid(grid: &Grid) {
    for row in grid {
        for col in row {
            if *col {
                print!("#");
            } else {
                print!(".")
            }
        }
        println!();
    }
}

fn main() {
    let init_state = parse_file("src/24.in");
    // part 1
    let biodiv_score = play_game(&init_state);
    println!("{}", biodiv_score);
}
