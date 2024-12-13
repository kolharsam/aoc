f = list(open("../../../inputs/input10", "r").readlines())
grid = []
for line in f:
    grid.append([int(x) for x in list(line.strip())])
