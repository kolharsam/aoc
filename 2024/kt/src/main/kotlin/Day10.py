from copy import deepcopy
from collections import deque

f = list(open("../../../inputs/input10", "r").readlines())
grid = []
for line in f:
    grid.append([int(x) for x in list(line.strip())])

# print(grid)

# Part 1

R = len(grid)
C = len(grid[0])
p1 = 0


def find_paths(r, c):
    q = deque()
    q.append((r, c))
    paths = 0
    visited = set()

    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if grid[r][c] == 0:
            paths += 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r = r + dr
            new_c = c + dc
            if (
                0 <= new_r < R
                and 0 <= new_c < C
                and grid[new_r][new_c] == grid[r][c] - 1
            ):
                q.append((new_r, new_c))
    return paths


p2 = 0
DP = {}


def find_paths2(r, c):
    if grid[r][c] == 0:
        return 1
    if (r, c) in DP:
        return DP[(r, c)]
    paths = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_r = r + dr
        new_c = c + dc
        if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] == grid[r][c] - 1:
            paths += find_paths2(new_r, new_c)
    DP[(r, c)] = paths
    return paths


for r in range(R):
    for c in range(C):
        if grid[r][c] == 9:
            p1 += find_paths(r, c)
            p2 += find_paths2(r, c)

print(p1)
print(p2)
