input = [line.split(", ") for line in open("input")][0]

loc = 0 + 0j
current_dir = 1j

# using complex numbers because you can represent them as cos(theta) + i.sin(theta) and act as coordinates for x & y
# on a 2-D graph
# at first we're facing the north hence current_dir = 1j since cos(90) = 0

for i in input:
    turn = i[0]
    times = int(i.split(turn)[1])
    if turn == 'R':
        current_dir *= -1j
    elif turn == 'L':
        current_dir *= 1j
    loc += current_dir * times

print(abs(loc.real) + abs(loc.imag)) # part 1 answer

VISITED = set()

loc = 0 + 0j
current_dir = 1j

for i in input:
    found = False
    turn = i[0]
    times = int(i.split(turn)[1])
    if turn == 'R':
        current_dir *= -1j
    elif turn == 'L':
        current_dir *= 1j
    for _ in range(times):
        loc += current_dir
        if loc in VISITED:
            print(abs(loc.real) + abs(loc.imag)) # answer for Part 2
            found = True
            break
        else:
            VISITED.add(loc)
    if found:
        break
