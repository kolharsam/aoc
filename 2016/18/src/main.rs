use std::fs;

fn parse_input(filename: &str) -> Vec<String> {
    let mut input: Vec<String> = Vec::new();
    let input_string = fs::read_to_string(filename).expect("Failed to open the file");
    let input_vec = input_string.split("").collect::<Vec<&str>>();

    for i in input_vec {
        input.push(i.to_string());
    }

    input
}

fn count_safe(row: &[String]) -> i32 {
    let current_row = row.to_owned();
    let mut safe = 0;

    for c in current_row {
        if c == "." {
            safe += 1;
        }
    }
    safe
}

fn make_next_row(current: &[String]) -> Vec<String> {
    let current_row = current.to_owned();
    let mut new_row: Vec<String> = Vec::new();
    let mut index = 0;

    new_row.push("".to_string());

    while index < current_row.len() - 2 {
        let left = &current_row[index];
        let right = &current_row[index + 2];
        let trap = "^";
        let safe = ".";

        if left == trap {
            if right != trap {
                new_row.push(trap.to_string());
            } else {
                new_row.push(safe.to_string());
            }
        } else if right == trap {
            if left != trap {
                new_row.push(trap.to_string());
            } else {
                new_row.push(safe.to_string());
            }
        } else {
            new_row.push(safe.to_string());
        }

        index += 1;
    }

    new_row.push("".to_string());

    new_row
}

fn form_pattern(init_pattern: &[String], rows: i32) -> i32 {
    let mut pattern = init_pattern.to_owned();
    let mut total_safe = 0;
    let mut count = 0;

    while count < rows {
        total_safe += count_safe(&pattern);
        pattern = make_next_row(&pattern);
        count += 1;
    }

    total_safe
}

fn main() {
    let pat = parse_input("src/18.in");
    let num_rows = 40;
    let num_rows_2 = 400000;
    // part 1
    println!("{}", form_pattern(&pat, num_rows));
    // part 2
    println!("{}", form_pattern(&pat, num_rows_2));
}
