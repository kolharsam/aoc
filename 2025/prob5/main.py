import sys

input_file = ""

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "input.example"

def read_input():
    file = open(input_file, "r")
    inputs = file.read().strip().split("\n\n")

    ing_ranges = inputs[0].split("\n")
    ranges = []

    for i in range(len(ing_ranges)):
        parts = ing_ranges[i].split("-")
        ranges.append((int(parts[0]), int(parts[1])))

    ings = list(map(int, inputs[1].split("\n")))

    return ranges, ings

def p1():
    ranges, ings = read_input()
    valid_ings = []
    
    for ing in ings:
        valid = False
        for r in ranges:
            if r[0] <= ing <= r[1]:
                valid = True
                valid_ings.append(ing)
                break
        if not valid:
            pass

    print(len(valid_ings))

def p2():
    valid_ings = set()
    ranges, _ = read_input()

    ranges.sort(key=lambda x: x[0])

    merged_ranges = []

    for cur_start, cur_end in ranges:
        if not merged_ranges:
            merged_ranges.append((cur_start, cur_end))
            continue

        last_start, last_end = merged_ranges[-1]

        if cur_start <= last_end + 1:
            new_end = max(last_end, cur_end)
            merged_ranges[-1] = (last_start, new_end)
        else:   
            merged_ranges.append((cur_start, cur_end))


    tot_valid_ings = 0

    for r in merged_ranges:
        tot_valid_ings += (r[1] - r[0] + 1)
    
    print(tot_valid_ings)

if __name__ == "__main__":
    p1()
    p2()
