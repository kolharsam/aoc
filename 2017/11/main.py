with open("input") as reader:
    input = reader.read()

input = input.split(",")

# this is based on the cubic coordinate system as described in here: https://www.redblobgames.com/grids/hexagons/#neighbors-cube
# reinventing the wheel may not be the best everytime. I was thinking of a stack based approach earlier and it had
# limitations in the case where inputs ne, ne, s, s is essentially -> (se, se) I couldn't wrap my head around this
# but the rest of the cases could be handled and the size of the stack would be my minimum distance

dirs = {
    "n"     : [0, 1, -1],                                                 
    "ne"    : [1, 0, -1],
    "nw"    : [-1, 1, 0],
    "s"     : [0, -1, 1],
    "se"    : [1, -1, 0],
    "sw"    : [-1, 0, 1]
}

start = [0, 0, 0]
max_start = 0

def Sum(arr1, arr2):
    return [arr1[x] + arr2[x] for x in range(3)]

def dis(arr):
    return max(abs(start[0]) , abs(start[1]), abs(start[2]))

for d in input:
    start = Sum(start, dirs[d])
    max_start = max(max_start, dis(start))

print(dis(start)) # part 1
print(max_start) # part 2
