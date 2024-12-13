# f = open("../../../inputs/input6", "r").readlines()

# grid = []
# for line in f:
#     grid.append(list(line.strip()))

# # print(grid)

# # Part 1
# R, C = len(grid), len(grid[0])
# pos = [0, 0]

# for i, r in enumerate(grid):
#     for j, _ in enumerate(r):
#         if grid[i][j] == "^":
#             pos[0] = i
#             pos[1] = j
#             break

# # print(pos, R, C)

# dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


# def turn_right(dr, dc):
#     # Turn right logic: new direction is (dc, -dr)
#     return dc, -dr


# def simulate(pos, grid, R, C):
#     visited = set([(pos[0], pos[1])])
#     r, c = pos
#     dr, dc = dirs[grid[r][c]]  # Get initial direction based on the grid value

#     while True:
#         nr, nc = r + dr, c + dc

#         # Check bounds
#         if nr < 0 or nr >= R or nc < 0 or nc >= C:
#             break

#         if grid[nr][nc] == "#":
#             # Turn right if hitting a wall
#             dr, dc = turn_right(dr, dc)
#         else:
#             # Continue in the current direction
#             r, c = nr, nc
#             visited.add((r, c))
#             continue

#         # Update position after turning
#         nr, nc = r + dr, c + dc
#         if nr < 0 or nr >= R or nc < 0 or nc >= C:
#             break
#         if grid[nr][nc] != "#":
#             r, c = nr, nc
#             visited.add((r, c))

#     return visited


# print(len(simulate(pos, grid, R, C)))  # Part 1

f = open("../../../inputs/input6-example", "r").readlines()

grid = []
for line in f:
    grid.append(list(line.strip()))

print(grid)

R, C = len(grid), len(grid[0])
start_pos = [0, 0]

# Locate the '^' starting position
for i, r in enumerate(grid):
    for j, _ in enumerate(r):
        if grid[i][j] == "^":
            start_pos = [i, j]
            break

print("Starting position:", start_pos)

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def turn_right(dr, dc):
    return dc, -dr


def simulate_with_obstruction(start_pos, grid, R, C, obstruction=None):
    visited = set()
    r, c = start_pos
    dr, dc = dirs[grid[r][c]]  # Starting direction

    while True:
        # Add the obstruction temporarily
        if obstruction:
            grid[obstruction[0]][obstruction[1]] = "#"

        nr, nc = r + dr, c + dc

        # Check bounds
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            break

        # If obstruction encountered
        if grid[nr][nc] == "#":
            dr, dc = turn_right(dr, dc)  # Turn right
        else:
            r, c = nr, nc
            if (r, c) in visited:
                # Infinite loop detected
                if obstruction:
                    grid[obstruction[0]][obstruction[1]] = "."  # Restore
                return True
            visited.add((r, c))
            continue

        # If out of bounds after turning
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            break

    # Restore the grid if obstruction was added
    if obstruction:
        grid[obstruction[0]][obstruction[1]] = "."

    return False


def find_obstruction_positions(grid, start_pos, R, C):
    valid_positions = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == ".":
                # Test if placing a '#' here creates an infinite loop
                if simulate_with_obstruction(start_pos, grid, R, C, (i, j)):
                    valid_positions.append((i, j))
    return valid_positions


# Find all valid positions to place '#'
positions = find_obstruction_positions(grid, start_pos, R, C)
print("Valid positions to place obstruction:", positions)
