# input_path = "../../../inputs/input4"

# try:
#     input = open(input_path, "r").readlines()
# except FileNotFoundError:
#     print(f"File not found: {input_path}")
#     exit(1)

# grid = [list(line.strip()) for line in input]

# R = len(grid)
# if R == 0:
#     print("Grid is empty")
#     exit(1)

# C = len(grid[0])

# dirs = {
#     "west": (0, -1),
#     "east": (0, 1),
#     "north": (-1, 0),
#     "south": (1, 0),
#     "northwest": (-1, -1),
#     "northeast": (-1, 1),
#     "southwest": (1, -1),
#     "southeast": (1, 1),
# }


# def check_xmas(r, c, direction):
#     """
#     Check if "XMAS" is formed starting at grid[r][c] in the given direction.
#     """
#     d = dirs[direction]
#     target = "MAS"
#     for i in range(len(target)):
#         r, c = r + d[0], c + d[1]
#         if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != target[i]:
#             return False
#     return True


# xmas_count = 0

# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == "X":
#             for direction in dirs:
#                 if check_xmas(r, c, direction):
#                     xmas_count += 1

# print(f"Total 'XMAS' found: {xmas_count}")


input_path = "../../../inputs/input4-example"

try:
    input = open(input_path, "r").readlines()
except FileNotFoundError:
    print(f"File not found: {input_path}")
    exit(1)

grid = [list(line.strip()) for line in input]

R = len(grid)
C = len(grid[0])


def is_pattern_match(r, c):
    """
    Check if the 3x3 pattern with center at (r, c) matches any of the following:
    M . S
    . A .
    M . S

    S . M
    . A .
    S . M

    S . S
    . A .
    M . M

    M . M
    . A .
    S . S
    """
    if grid[r][c] != "A":
        return False

    # Ensure within bounds for a 3x3 region
    if r - 1 < 0 or c - 1 < 0 or r + 1 >= R or c + 1 >= C:
        return False

    # Extract the surrounding 3x3 region
    top_left = grid[r - 1][c - 1]
    top_right = grid[r - 1][c + 1]
    bottom_left = grid[r + 1][c - 1]
    bottom_right = grid[r + 1][c + 1]

    # Check all four patterns explicitly
    return (
        (
            top_left == "M"
            and top_right == "S"
            and bottom_left == "M"
            and bottom_right == "S"
        )
        or (
            top_left == "S"
            and top_right == "M"
            and bottom_left == "S"
            and bottom_right == "M"
        )
        or (
            top_left == "S"
            and top_right == "S"
            and bottom_left == "M"
            and bottom_right == "M"
        )
        or (
            top_left == "M"
            and top_right == "M"
            and bottom_left == "S"
            and bottom_right == "S"
        )
    )


pattern_count = 0

for r in range(R):
    for c in range(C):
        if is_pattern_match(r, c):
            pattern_count += 1

print(f"Total matching patterns found: {pattern_count}")
