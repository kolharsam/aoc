# import re
# import numpy as np  # type: ignore
# import os
# import time

# robot = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

# f = open("../../../inputs/input14", "r").read().split("\n")

# robots = []

# X = 101
# Y = 103

# for line in f:
#     m = re.match(robot, line.strip())
#     if not m:
#         continue
#     nums = m.groups()
#     print(nums)
#     robots.append(
#         {
#             "p": [int(nums[0]), int(nums[1])],
#             "v": [int(nums[2]), int(nums[3])],
#         }
#     )

# cq1 = cq2 = cq3 = cq4 = 0
# mx = X // 2
# my = Y // 2


# def clear_screen():
#     """Clear the terminal screen."""
#     # Use appropriate clear command based on operating system
#     os.system("cls" if os.name == "nt" else "clear")


# for t in range(10**6):
#     G = [["." for _ in range(X)] for _ in range(Y)]
#     for i, robot in enumerate(robots):
#         robot["p"][0] += robot["v"][0]
#         robot["p"][1] += robot["v"][1]
#         robot["p"][0] %= X
#         robot["p"][1] %= Y
#         # robots[i] = robot
#         G[robot["p"][1]][robot["p"][0]] = "#"

#         # if t == 99:
#         #     if robot["p"][0] < mx and robot["p"][1] < my:
#         #         cq1 += 1
#         #     elif robot["p"][0] > mx and robot["p"][1] < my:
#         #         cq2 += 1
#         #     elif robot["p"][0] < mx and robot["p"][1] > my:
#         #         cq3 += 1
#         #     elif robot["p"][0] > mx and robot["p"][1] > my:
#         #         cq4 += 1
#     if t >= 5676:
#         clear_screen()
#         for i in range(Y):
#             print("".join(G[i]))
#         print("\n", t, "\n")
#         time.sleep(0.5)

# # print(cq1 * cq2 * cq3 * cq4)
import re
import os
import time
from colorama import init, Fore, Style


init()

robot = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"
f = open("../../../inputs/input14", "r").read().split("\n")

robots = []
X = 101
Y = 103
DOWNSCALE_FACTOR = 1

for line in f:
    m = re.match(robot, line.strip())
    if not m:
        continue
    nums = m.groups()
    robots.append(
        {
            "p": [int(nums[0]), int(nums[1])],
            "v": [int(nums[2]), int(nums[3])],
        }
    )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_downsampled_grid(grid, factor):
    downsampled = []
    for y in range(0, len(grid), factor):
        row = []
        for x in range(0, len(grid[0]), factor):
            # Check for boundaries and combine cells
            if any(
                grid[yy][xx] == "#"
                for yy in range(y, min(y + factor, len(grid)))
                for xx in range(x, min(x + factor, len(grid[0])))
            ):
                row.append("#")
            else:
                row.append(" ")
        downsampled.append(row)
    for row in downsampled:
        for cell in row:
            if cell == "#":
                print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "█", end="")
            else:
                print(Style.RESET_ALL + " ", end="")
        print(Style.RESET_ALL)


for t in range(10**6):
    G = [[" " for _ in range(X)] for _ in range(Y)]
    for robot in robots:
        # Update position
        robot["p"][0] += robot["v"][0]
        robot["p"][1] += robot["v"][1]
        robot["p"][0] %= X
        robot["p"][1] %= Y
        G[robot["p"][1]][robot["p"][0]] = "#"

    if t >= 7070:
        clear_screen()
        print_downsampled_grid(G, DOWNSCALE_FACTOR)
        print(f"\nTime: {t}\n")
        time.sleep(1)
