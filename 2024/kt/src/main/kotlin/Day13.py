import re
import numpy as np  # type: ignore

r_button = r"(Button\s+(A|B)):\s+X\+(\d+),\s+Y\+(\d+)"
r_gift = r"Prize: X=(\d+), Y=(\d+)"

f = open("../../../inputs/input13", "r").read().split("\n\n")

buttons = []

for line in f:
    button = {}
    fsp = line.split("\n")
    b1 = re.match(r_button, fsp[0])
    b1g = b1.groups()
    button["A"] = [int(b1g[2]), int(b1g[3])]
    b2 = re.match(r_button, fsp[1])
    b2g = b2.groups()
    button["B"] = [int(b2g[2]), int(b2g[3])]
    g = re.match(r_gift, fsp[2])
    gg = g.groups()
    button["gift"] = [int(gg[0]), int(gg[1])]
    buttons.append(button)


def solve(coeffs, consts):
    try:
        solution = np.linalg.solve(coeffs, consts)
        return np.round(solution, decimals=3)
    except np.linalg.LinAlgError as e:
        print("Error solving the equation:", e)
        exit(1)


def is_whole_number(n, tol=1e-15):
    return np.mod(n, 1) == 0


cost = 0

for button in buttons:
    A = np.array(
        [[button["A"][0], button["B"][0]], [button["A"][1], button["B"][1]]],
        dtype=np.int64,
    )
    B = np.array(
        [10**13 + button["gift"][0], 10**13 + button["gift"][1]], dtype=np.int64
    )
    x, y = solve(A, B)
    if is_whole_number(x) and is_whole_number(y):
        cost += (3 * x) + y

print(cost)
