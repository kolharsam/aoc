import sys

input_file = ""

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "input.example"

def read_input():
    file = open(input_file, "r")
    return file.read().strip().split("\n")

def process_bank(bank):
    n = len(bank)
    num = 0
    
    for i in range(n-1):
        curr = int(bank[i])
        max_in_next = max(bank[i+1:])

        curr_num = (curr * 10) + int(max_in_next)

        num = max(num, curr_num)
    
    return num

def process_bank_p2(bank):
    pass

def p1():
    banks = read_input()
    s = 0
    
    for bank in banks:
        s += process_bank(bank)
    
    print(s)

def p2():
    process_bank_p2(0)
    pass

if __name__ == "__main__":
    p1()
    p2()
