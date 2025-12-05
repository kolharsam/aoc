import sys

input_file = ""

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "input.example"

def read_input():
    file = open(input_file, "r")
    return file.read().strip().split("\n")

def p1():
    lines = read_input()
    print(lines)

def p2():
    pass

if __name__ == "__main__":
    p1()
    p2()
