use std::collections::HashMap;
use std::fs;

#[derive(Debug, Copy, Clone, PartialEq, Eq, Hash)]
struct Coordinate {
    x: i32,
    y: i32,
    z: i32,
}

#[derive(Debug, Copy, Clone)]
struct Particle {
    id: i32,
    position: Coordinate,
    acceleration: Coordinate,
    velocity: Coordinate,
}

impl Particle {
    fn tick(&self) -> Particle {
        Particle {
            id: self.id,
            position: Coordinate {
                x: self.position.x + self.velocity.x + self.acceleration.x,
                y: self.position.y + self.velocity.y + self.acceleration.y,
                z: self.position.z + self.velocity.z + self.acceleration.z,
            },
            acceleration: self.acceleration,
            velocity: Coordinate {
                x: self.velocity.x + self.acceleration.x,
                y: self.velocity.y + self.acceleration.y,
                z: self.velocity.z + self.acceleration.z,
            },
        }
    }

    fn manhattan_distance(&self) -> i32 {
        self.position.x.abs() + self.position.y.abs() + self.position.z.abs()
    }
}

fn convert_to_number(str_num: &str) -> i32 {
    let num: i32 = String::from(str_num).parse().unwrap();
    num
}

fn parse_coordinates(split_str: &str) -> Coordinate {
    // NOTE: would've been better to split the whole thing using regex
    let split_str_string = split_str.to_string();
    let p1_split = split_str_string.split("=<").collect::<Vec<&str>>();
    let p1_split_string = p1_split[1].to_string();
    let p2_split = p1_split_string.split('>').collect::<Vec<&str>>();
    let p2_split_string = p2_split[0].to_string();
    let numbers = p2_split_string.split(',').collect::<Vec<&str>>();
    let x = convert_to_number(numbers[0]);
    let y = convert_to_number(numbers[1]);
    let z = convert_to_number(numbers[2]);

    Coordinate { x, y, z }
}

fn parse_input(filename: &str) -> Result<Vec<Particle>, &str> {
    let buf = fs::read_to_string(filename).expect("There was an error in opening the file");
    let mut particles: Vec<Particle> = Vec::new();

    for (id, l) in buf.split('\n').enumerate() {
        let line_string = l.to_string();
        let splits = line_string.split(", ").collect::<Vec<&str>>();
        let position = parse_coordinates(splits[0]);
        let velocity = parse_coordinates(splits[1]);
        let acceleration = parse_coordinates(splits[2]);

        particles.push(Particle {
            id: id as i32,
            position,
            velocity,
            acceleration,
        });
    }

    Ok(particles)
}

fn update_particles(current_particles: &[Particle]) -> Vec<Particle> {
    let mut new_particles = current_particles.to_owned();

    for (pos, particle) in current_particles.iter().enumerate() {
        let new_particle = particle.tick();
        new_particles[pos] = new_particle;
    }

    new_particles
}

fn collide_update_particles(cps: &[Particle]) -> Vec<Particle> {
    let current_particles = cps.to_owned();
    let mut new_particles: Vec<Particle> = Vec::new();
    let mut count = 0;
    let mut positions_map: HashMap<Coordinate, i32> = HashMap::new();

    while count < current_particles.len() {
        if !positions_map.contains_key(&current_particles[count].position) {
            positions_map.insert(current_particles[count].position, 1);
        } else {
            positions_map.insert(
                current_particles[count].position,
                1 + positions_map[&current_particles[count].position],
            );
        }
        count += 1;
    }

    count = 0;

    while count < current_particles.len() {
        let particle_on_top: Particle = current_particles[count];
        let num_count = positions_map[&particle_on_top.position];
        if num_count == 1 {
            new_particles.push(particle_on_top);
        }
        count += 1;
    }

    new_particles
}

fn main() {
    let mut all_particles = parse_input("src/20.in").unwrap();
    let mut all_particles_p2 = all_particles.clone();
    let mut closest: i32 = 0;
    let mut closest_id: i32 = 0;
    let mut times = 0;

    while times <= 5000 {
        let for_iters = all_particles.clone();
        let mut local_closest: i32 = 1000000000;
        let mut local_closest_id: i32 = 0;

        for particle in for_iters {
            let manhat_distance = particle.manhattan_distance();
            if local_closest > manhat_distance {
                local_closest_id = particle.id;
                local_closest = manhat_distance;
            }
        }

        closest = local_closest;
        closest_id = local_closest_id;
        times += 1;

        let updated_particles = update_particles(&all_particles);
        let p2_udpated_particles = collide_update_particles(&all_particles_p2);
        let updated_particles_p2 = update_particles(&p2_udpated_particles);
        all_particles = updated_particles;
        all_particles_p2 = updated_particles_p2;
    }

    // part 1
    println!("{}: {}", closest_id, closest);
    // part 2
    println!("{}", all_particles_p2.len());
}
