extern crate rand;
use rand::seq::SliceRandom;
use rand::thread_rng;
use std::fs::read_to_string;

// NOTE: I did try using just `str` but failed to understand the error
// that was a lifetime error, and basically the `not live long enough error`
#[derive(PartialEq, Debug, Copy, Clone)]
enum Instruction {
    SwapByLetter {
        x: char,
        y: char,
    },
    SwapByPosition {
        x: i32,
        y: i32,
    },
    RotateByDirection {
        steps: i32,
        direction: RotateDirection,
    },
    RotateByLetter {
        letter: char,
    },
    ReverseOrder {
        x: i32,
        y: i32,
    },
    MoveLetter {
        x: i32,
        y: i32,
    },
}

#[derive(PartialEq, Debug, Copy, Clone)]
enum RotateDirection {
    Left,
    Right,
}

fn convert_to_number(i: &str) -> i32 {
    return i.to_string().parse::<i32>().unwrap();
}

fn get_letter_position(letters: &[String], letter: &str) -> usize {
    letters
        .iter()
        .position(|r| r == &letter.to_string())
        .unwrap()
}

fn swap_position(current: &[String], x: usize, y: usize) -> Vec<String> {
    let mut updated_position = current.to_owned();
    updated_position.swap(x, y);
    updated_position
}

fn swap_letter(current: &[String], let1: &str, let2: &str) -> Vec<String> {
    let letters = current.to_owned();
    let pos1 = get_letter_position(&letters, let1);
    let pos2 = get_letter_position(&letters, let2);
    return swap_position(&letters, pos1, pos2);
}

fn rotate_by_dir(current: &[String], dir: RotateDirection, times: usize) -> Vec<String> {
    let mut letters = current.to_owned();

    if dir == RotateDirection::Left {
        letters.rotate_left(times);
    } else {
        letters.rotate_right(times);
    }

    letters
}

fn rotate_by_letter(current: &[String], letter: &str) -> Vec<String> {
    let letters = current.to_owned();
    let pos = get_letter_position(&letters, letter);
    let mut times: usize = 1 + pos;

    if pos >= 4 {
        times += 1;
    }

    return rotate_by_dir(&letters, RotateDirection::Right, times % letters.len());
}

fn reverse_substr(current: &[String], let1: i32, let2: i32) -> Vec<String> {
    let letters = current.to_owned();
    let bef_slice = letters[0..(let1 as usize)].to_vec();
    let aft_slice = letters[((let2 + 1) as usize)..].to_vec();
    let mut slice = letters[(let1 as usize)..((let2 + 1) as usize)].to_vec();
    slice.reverse();
    let mut new_letters: Vec<String> = Vec::new();

    [bef_slice, slice, aft_slice]
        .to_vec()
        .iter()
        .for_each(|sl| {
            sl.iter().for_each(|l| {
                new_letters.push(l.to_string());
            });
        });

    new_letters
}

fn move_str(current: &[String], let1: i32, let2: i32) -> Vec<String> {
    let letters = current.to_owned();
    let mut letters_copy = letters.clone();
    let to_add = &letters[let1 as usize];
    letters_copy.remove(let1 as usize);
    letters_copy.insert(let2 as usize, to_add.to_string());

    letters_copy
}

fn scrambled_password(init: &str, inst: &[Instruction]) -> String {
    let mut letters: Vec<String> = Vec::new();
    for letter in init.to_string().split("").collect::<Vec<&str>>() {
        if letter != "" {
            letters.push(letter.to_string());
        }
    }

    for &i in inst {
        match i {
            Instruction::RotateByLetter { letter } => {
                letters = rotate_by_letter(&letters, &letter.to_string());
            }
            Instruction::ReverseOrder { x, y } => {
                letters = reverse_substr(&letters, x, y);
            }
            Instruction::MoveLetter { x, y } => {
                letters = move_str(&letters, x, y);
            }
            Instruction::SwapByPosition { x, y } => {
                letters = swap_position(&letters, x as usize, y as usize);
            }
            Instruction::SwapByLetter { x, y } => {
                letters = swap_letter(&letters, &x.to_string(), &y.to_string());
            }
            Instruction::RotateByDirection { direction, steps } => {
                letters = rotate_by_dir(&letters, direction, steps as usize);
            }
        }
    }

    let mut res = String::new();
    for letter in letters {
        let ch: Vec<char> = letter.chars().collect();
        res.push(ch[0]);
    }
    res
}

fn parse_file(filename: &str) -> Vec<Instruction> {
    let file_str = read_to_string(filename).expect("Failed to open the file");
    let str_split = file_str.split('\n').collect::<Vec<&str>>();
    let mut lines: Vec<String> = Vec::new();
    let mut instructions: Vec<Instruction> = Vec::new();

    for st in str_split {
        lines.push(st.to_string());
    }

    lines.iter().for_each(|line| {
        let line_split = line.split(' ').collect::<Vec<&str>>();
        if line.contains("swap") {
            if line.contains("position") {
                let pos1 = convert_to_number(line_split[2]);
                let pos2 = convert_to_number(line_split[5]);
                instructions.push(Instruction::SwapByPosition { x: pos1, y: pos2 });
            } else {
                let let1: Vec<char> = line_split[2].chars().collect();
                let let2: Vec<char> = line_split[5].chars().collect();
                instructions.push(Instruction::SwapByLetter {
                    x: let1[0],
                    y: let2[0],
                });
            }
        } else if line.contains("rotate") {
            if line.contains("step") {
                let steps = convert_to_number(line_split[2]);
                if line_split[1] == "right" {
                    instructions.push(Instruction::RotateByDirection {
                        direction: RotateDirection::Right,
                        steps,
                    });
                } else {
                    instructions.push(Instruction::RotateByDirection {
                        direction: RotateDirection::Left,
                        steps,
                    });
                }
            } else {
                let letter: Vec<char> = line_split[6].chars().collect();
                instructions.push(Instruction::RotateByLetter { letter: letter[0] });
            }
        } else if line.contains("reverse") {
            let let1 = convert_to_number(line_split[2]);
            let let2 = convert_to_number(line_split[4]);
            instructions.push(Instruction::ReverseOrder { x: let1, y: let2 });
        } else {
            let x = convert_to_number(line_split[2]);
            let y = convert_to_number(line_split[5]);
            instructions.push(Instruction::MoveLetter { x, y });
        }
    });

    instructions
}

fn new_test(t: &[String]) -> Vec<String> {
    let mut current_test = t.to_owned();
    let mut rng = thread_rng();
    current_test.shuffle(&mut rng);
    current_test
}

fn main() {
    let instructions = parse_file("src/21.in");
    let input = "abcdefgh";
    let input2 = "fbgdceah";
    // part 1
    let scrambled = scrambled_password(&input, &instructions);
    println!("{}", scrambled);
    // part 2 - maybe not the best way, but certainly is one of the ways to do it
    // reverse engineering the whole thing is tricky when it comes to the part where
    // used to rotate by a letter, and this solution definitely depends on the permutations
    // that are generated at random, so yeah the time it would take to complete
    // this is very unclear
    let inp_split = input.split("").collect::<Vec<&str>>();
    let mut test: Vec<String> = Vec::new();
    for inp in inp_split {
        if inp != "" {
            test.push(inp.to_string());
        }
    }
    loop {
        let test_str = test.join("");
        let unscrambled = scrambled_password(&test_str, &instructions);
        if unscrambled == input2 {
            break;
        }
        test = new_test(&test);
    }
    println!("{}", test.join(""));
}
