use std::fs::read_to_string;

const NEED_SPACE: u64 = 30_000_000;
const TOTAL_SPACE: u64 = 70_000_000;
const SIZE_THRESHOLD: u64 = 100_000;

fn main() {
    println!("part1: {}", part1());
    println!("part2: {}", part2());
}

fn part1() -> u64 {
    let mut d: Digger = Digger {
        cur_idx: 0,
        size: 0,
        smallest: 0,
        rows: read_to_string("./day7").
            unwrap().
            split('\n').
            map(|s| s.to_string()).
            collect(),
    };

    d.sum_of_small("/".to_string());

    return d.size;
}

fn part2() -> u64 {
    let mut d: Digger = Digger {
        cur_idx: 0,
        size: 0,
        smallest: NEED_SPACE,
        rows: read_to_string("./day7").
            unwrap().
            split('\n').
            map(|s| s.to_string()).
            collect(),
    };

    let total_used = d.total_used();
    let space_to_find = NEED_SPACE - (TOTAL_SPACE - total_used);
    let smallest = d.smallest_to_delete(space_to_find, "/".to_string());

    return smallest;
}

struct Digger {
    size: u64,
    smallest: u64,
    rows: Vec<String>,
    cur_idx: usize,
}

impl Digger {
    pub fn total_used(&mut self) -> u64 {
        let mut total: u64 = 0;

        for row in self.rows.iter() {
            if is_file(row.as_str()) {
                let (size, _) = file_info(row.as_str());

                total += size;
            }
        }

        return total;
    }

    pub fn sum_of_small(&mut self, path: String) -> u64 {
        println!("AT {}", path);

        let mut dir_size: u64 = 0;

        loop {
            if self.cur_idx >= self.rows.len() {
                break;
            }

            let row = self.rows[self.cur_idx].as_str();

            println!("{}", self.cur_idx);

            if is_file(row) {
                let (size, name) = file_info(row);

                dir_size += size;

                self.cur_idx += 1;
                continue;
            }

            if row == "$ cd /" || row == "$ ls" || row.starts_with("dir") {
                self.cur_idx += 1;
                continue;
            }

            if row == "$ cd .." {
                if dir_size <= SIZE_THRESHOLD {
                    self.size += dir_size;
                }

                self.cur_idx += 1;

                println!("Exiting by .. {}", path);

                return dir_size;
            }

            if row.starts_with("$ cd") {
                self.cur_idx += 1;
                let dir_to_go = dir_name(row).to_string();

                dir_size += self.sum_of_small(dir_to_go);
            }
        }

        if dir_size <= SIZE_THRESHOLD {
            self.size += dir_size;
        }

        println!("Exiting by end {}", path);

        return dir_size;
    }

    pub fn smallest_to_delete(&mut self, space_to_find: u64, path: String) -> u64 {
        println!("AT {}", path);

        let mut row: &str = "";
        let mut dir_size: u64 = 0;

        loop {
            if self.cur_idx >= self.rows.len() {
                break;
            }

            row = self.rows[self.cur_idx].as_str();

            println!("{}", self.cur_idx);

            if is_file(row) {
                let (size, name) = file_info(row);

                dir_size += size;

                self.cur_idx += 1;
                continue;
            }

            if row == "$ cd /" || row == "$ ls" || row.starts_with("dir") {
                self.cur_idx += 1;
                continue;
            }

            if row == "$ cd .." {
                if dir_size >= space_to_find && dir_size < self.smallest {
                    self.smallest = dir_size
                }

                self.cur_idx += 1;

                println!("Exiting by .. {}", path);

                return dir_size;
            }

            if row.starts_with("$ cd") {
                self.cur_idx += 1;
                let dir_to_go = dir_name(row).to_string();

                dir_size += self.smallest_to_delete(space_to_find, dir_to_go);
            }
        }

        if dir_size >= space_to_find && dir_size < self.smallest {
            self.smallest = dir_size
        }

        println!("Exiting by end {}", path);

        return dir_size;
    }
}


fn is_cmd(inp: &str) -> bool {
    return inp.starts_with("$ ");
}

fn cd_dir(inp: &str) -> &str {
    let mut coll = inp.split_whitespace();
    coll.next();
    coll.next();

    return coll.next().unwrap();
}

fn dir_name(inp: &str) -> &str {
    let mut coll = inp.split_whitespace();

    coll.next();
    coll.next();

    return coll.next().unwrap();
}

fn is_file(inp: &str) -> bool {
    match inp.split_whitespace().next().ok_or("unable to split") {
        Ok(v) => match v.parse::<u64>() {
            Ok(_) => return true,
            Err(_) => return false,
        },
        Err(_) => return false,
    }
}

fn file_info(inp: &str) -> (u64, &str) {
    let mut size: u64 = 0;
    let mut name: &str = "";
    let mut parts = inp.split_whitespace();

    match parts.next().
        ok_or("unable to split") {
        Ok(v) => match v.parse::<u64>() {
            Ok(uval) => {
                size = uval;
                name = parts.next().unwrap();
            }
            _ => {}
        },

        _ => {}
    }

    return (size, name);
}
