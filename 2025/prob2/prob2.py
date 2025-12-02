import sys

input_file = ""

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "input.example"

def read_input():
    file = open(input_file, "r")
    return file.read().strip().split("\n")[0].split(",")

def is_even_length(num):
    return len(str(num)) % 2 == 0

def is_equal_on_both_halves(num):
    if not is_even_length(num):
        return False
    
    num_str = str(num)
    length = len(num_str)
    half = length // 2

    first_half = num_str[:half]
    second_half = num_str[half:]

    return first_half == second_half

def split_number_in_n_parts(num, n):
    num_str = str(num)
    length = len(num_str)
    part_length = length // n
    parts = []

    for i in range(n):
        start_index = i * part_length
        end_index = start_index + part_length
        parts.append(num_str[start_index:end_index])
    
    return parts

def has_repeated_sequence(num):
    num_str = str(num)
    length = len(num_str)

    for seq_len in range(1, length // 2 + 1):
        if length % seq_len != 0:
            continue
        
        parts = split_number_in_n_parts(num, length // seq_len)
        first_part = parts[0]

        if all(part == first_part for part in parts):
            return True
    return False

def p1():
    ranges = read_input()
    invalidIds = 0
    
    for rnge in ranges:
        start_str, end_str = rnge.split("-")
        start, end = int(start_str), int(end_str)

        for num in range(start, end + 1):
            if is_equal_on_both_halves(num):
                invalidIds += num
        
    print(invalidIds)

def p2():
    ranges = read_input()
    invalidIds = 0
    
    for rnge in ranges:
        start_str, end_str = rnge.split("-")
        start, end = int(start_str), int(end_str)

        for num in range(start, end + 1):
            if is_equal_on_both_halves(num) or has_repeated_sequence(num):
                invalidIds += num
        
    print(invalidIds)

if __name__ == "__main__":
    p1()
    p2()
