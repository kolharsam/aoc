use std::collections::HashMap;
use std::fs::read_to_string;

const EMPTY: char = '.';
const TREE: char = '#';

// NOTE: could've optimised this to use HashSet of
// only the positions of the tree present in the state
// or just as a string
type Gen = Vec<(i32, char)>;
type TreeSeq = Vec<char>;

struct TreeApp {
    gen_map: HashMap<TreeSeq, char>,
    generations: Vec<Gen>,
    state: Gen,
}

impl TreeApp {
    fn check_gen_map(&self, tree_seq: TreeSeq) -> char {
        if self.gen_map.contains_key(&tree_seq) {
            return *self.gen_map.get(&tree_seq).expect("unexpected error");
        }

        EMPTY
    }

    fn _print(&self) {
        for (i, gen) in self.generations.iter().enumerate() {
            print!("{}: ", i);
            for dot in gen {
                if dot.0 == 0 {
                    print!("({} {})", 0, dot.1);
                } else {
                    print!("{}", dot.1);
                }
            }
            println!();
        }
    }

    fn calc_plant_sum(&self) -> i32 {
        let mut tree_count = 0;
        for tree in self.state.iter() {
            if tree.1 == TREE {
                tree_count += tree.0;
            }
        }

        tree_count
    }

    fn find_tree(&self, pos: i32) -> (i32, char) {
        for i in self.state.iter() {
            if i.0 == pos {
                return *i;
            }
        }

        (i32::MIN, EMPTY)
    }

    fn calculate_next_state(&mut self) {
        let mut next_state = Gen::new();

        for tree_state in self.state.clone() {
            let pos = tree_state.0;
            let rt1 = self.find_tree(pos + 1);
            let rt2 = self.find_tree(pos + 2);
            let lt1 = self.find_tree(pos - 1);
            let lt2 = self.find_tree(pos - 2);

            if lt1.0 == i32::MIN && lt2.0 == i32::MIN && lt1.1 == EMPTY && lt2.1 == EMPTY {
                next_state.push((pos - 1, lt2.1));
                next_state.push((pos - 2, lt1.1));
            }

            let tree_vec = vec![lt2, lt1, tree_state, rt1, rt2];
            let tree_seq: TreeSeq = tree_vec.into_iter().map(|x| x.1).collect();
            let next_tree_state = self.check_gen_map(tree_seq);
            next_state.push((pos, next_tree_state));

            if rt1.0 == i32::MIN && rt2.0 == i32::MIN && rt1.1 == EMPTY && rt2.1 == EMPTY {
                next_state.push((pos + 1, rt1.1));
                next_state.push((pos + 2, rt2.1));
            }
        }

        self.generations.push(next_state.clone());
        self.state = next_state;
    }
}

fn create_state(input_read: &[char]) -> Gen {
    let state_res = input_read
        .iter()
        .enumerate()
        .fold(Gen::new(), |mut l, (i, x)| {
            l.push((i as i32, *x));
            l
        });

    state_res
}

fn read_input(filename: &str) -> TreeApp {
    let file = read_to_string(filename).expect("failed to read the input file");
    let file_parts = file.split("\n\n").collect::<Vec<&str>>();
    let init_state_part = file_parts[0];
    let generator_fn_lines = file_parts[1].split('\n').collect::<Vec<&str>>();

    let init_state_parts: Vec<&str> = init_state_part.split(": ").collect();
    let init_state_line: TreeSeq = init_state_parts[1].chars().collect();
    let init_state = create_state(&init_state_line);

    let mut gen_map: HashMap<TreeSeq, char> = HashMap::new();
    for line in generator_fn_lines {
        let gen_line_split: Vec<&str> = line.split(" => ").collect();
        let gen_seq: TreeSeq = gen_line_split[0].chars().collect();
        let gen_result_char = gen_line_split[1].chars().collect::<Vec<char>>()[0];
        gen_map.insert(gen_seq, gen_result_char);
    }

    TreeApp {
        gen_map,
        state: init_state,
        generations: vec![create_state(&init_state_line)],
    }
}

fn main() {
    let mut app_context = read_input("input");
    for _ in 0..=19 {
        app_context.calculate_next_state();
    }
    // PART 1
    println!("{}", app_context.calc_plant_sum());
}
