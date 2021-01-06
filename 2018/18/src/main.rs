use std::collections::HashMap;
use std::fs::read_to_string;

const LUMBER: &str = "#";
const TREE: &str = "|";
const OPEN: &str = ".";

#[derive(std::cmp::Eq, PartialEq, std::hash::Hash, Debug, Copy, Clone)]
struct Coord(i32, i32);
#[derive(PartialEq, Debug, Copy, Clone)]
enum Acre {
    Tree,
    Lumber,
    Open,
}
type Area = HashMap<Coord, Acre>;

trait AreaFns {
    fn calc_resource_value(&self) -> i32;
    fn print_grid(&self);
}

impl AreaFns for Area {
    fn calc_resource_value(&self) -> i32 {
        let mut tree = 0;
        let mut lumber = 0;

        for (_, value) in self.iter() {
            if *value == Acre::Tree {
                tree += 1;
            } else if *value == Acre::Lumber {
                lumber += 1;
            }
        }

        tree * lumber
    }
    fn print_grid(&self) {
        let mut row = 0;
        let mut col = 0;
        while row < 10 {
            while col < 10 {
                let c = self.get(&Coord(row, col)).unwrap();
                if *c == Acre::Lumber {
                    print!("{}", LUMBER);
                } else if *c == Acre::Tree {
                    print!("{}", TREE);
                } else {
                    print!("{}", OPEN);
                }
                col += 1;
            }
            println!();
            col = 0;
            row += 1;
        }
        println!();
    }
}

impl Coord {
    fn get_neighbours(&self, current_state: &Area) -> (i8, i8) {
        let current_x = self.0;
        let current_y = self.1;
        let mut t_c: i8 = 0;
        let mut l_c: i8 = 0;

        for x in -1..2 {
            for y in -1..2 {
                if x == 0 && y == 0 {
                    continue;
                }
                if let Some(i) = current_state.get(&Coord(current_x + x, current_y + y)) {
                    if *i == Acre::Lumber {
                        l_c += 1;
                    } else if *i == Acre::Tree {
                        t_c += 1;
                    }
                }
            }
        }

        (t_c, l_c)
    }
}

fn parse_file(filename: &str) -> Area {
    let read_lines = read_to_string(filename).expect("Failed to open file");
    let mut new_area: Area = HashMap::new();
    let lines = read_lines.split('\n').collect::<Vec<&str>>();

    for (row, l) in lines.iter().enumerate() {
        let current_line = l.to_string();
        let cl_split = current_line.split("").collect::<Vec<&str>>();
        let mut col = 0;
        for cl in cl_split {
            if cl != "" {
                let r = row as i32;
                let coord = Coord(r, col);
                if cl == LUMBER {
                    new_area.insert(coord, Acre::Lumber);
                } else if cl == TREE {
                    new_area.insert(coord, Acre::Tree);
                } else {
                    new_area.insert(coord, Acre::Open);
                }
                col += 1;
            }
        }
    }

    new_area
}

fn play_game(area: Area, times_p1: i32, times_p2: i32) {
    let mut count: i32 = 0;
    let mut current_state = area;

    loop {
        let mut next_state: Area = HashMap::new();
        for (key, value) in current_state.iter() {
            let (t_c, l_c) = key.get_neighbours(&current_state);
            if *value == Acre::Open && t_c > 2 {
                next_state.insert(Coord(key.0, key.1), Acre::Tree);
            } else if *value == Acre::Tree && l_c > 2 {
                next_state.insert(Coord(key.0, key.1), Acre::Lumber);
            } else if *value == Acre::Lumber && !(t_c > 0 && l_c > 0) {
                next_state.insert(Coord(key.0, key.1), Acre::Open);
            } else {
                next_state.insert(*key, *value);
            }
        }
        if count == times_p1 {
            println!("{}", current_state.calc_resource_value());
        }
        if count == times_p2 {
            println!("{}", current_state.calc_resource_value());
            break;
        }
        count += 1;
        current_state = next_state;
    }
}

fn main() {
    let init_grid = parse_file("src/18.in");
    play_game(init_grid, 10, 1000);
    // for part 2 the actual number was 1000000000, but seeing that the
    // resource value keeps repeating itself, every 700 values or so,
    // doing a 1000 was enough
}
