# f = list(open("../../../inputs/input9-example", "r").readlines()[0].strip())
# # f = list(open("../../../inputs/input9", "r").readlines()[0].strip())

# p1 = []

# s = 0
# dot = False

# for i in f:
#     ii = int(i)
#     if not dot:
#         p1.extend([str(s)] * ii)
#         dot = True
#         s += 1
#     else:
#         p1.extend(["."] * ii)
#         dot = False

# # print(p1)

# # sps = "".join(p1)  # spaced out file
# # sp = list(sps)  # spaced out file as list
# # print(sp)
# left = 0
# right = len(p1) - 1

# while left < right:
#     # Find the next '.' on the left
#     while left < right and p1[left] != ".":
#         left += 1
#     # Find the next non-'.' on the right
#     while left < right and p1[right] == ".":
#         right -= 1
#     # Swap if valid indices
#     if left < right:
#         p1[left], p1[right] = p1[right], p1[left]
#         left += 1
#         right -= 1

# # print(sp)

# # print("".join(sp))

# checksum = 0
# for i, n in enumerate(p1):
#     if n != ".":
#         ii = int(n)
#         checksum += ii * i

# print(checksum)  # part 1

# p2 = []
# s = 0
# dot = False
# for i in f:
#     ii = int(i)
#     if not dot:
#         p2.append([str(s)] * ii)
#         dot = True
#         s += 1
#     else:
#         if ii != 0:
#             p2.append(["."] * ii)
#         dot = False

# for i in range(len(p2)):
#     l = 0
#     for ii in p2[i]:
#         if ii == ".":
#             l += 1
#     p2[i] = [p2[i], l, 0]

# # print(p2)

# # right = len(p2) - 1
# # p2l = len(p2) - 1
# # spaces = {}

# # while right >= 0:
# #     while p2[right][1] != 0 and spaces[right] == False:
# #         right -= 1
# #     space_needed = len(p2[right][0])
# #     spaces[right] = False
# #     for i in range(p2l):
# #         if p2[i][1] != 0 and p2[i][1] >= space_needed:
# #             for j in range(len(p2[right][0])):
# #                 print(i, right, space_needed)
# #                 p2[i][0][j + p2[i][2]] = p2[right][0][j]
# #             p2[i][1] -= space_needed
# #             p2[i][2] += space_needed
# #             p2[right][1] = space_needed
# #             p2[right][0] = ["."] * space_needed
# #             # right -= 1
# #             spaces[right] = True
# #             break


# # print(p2)

# right = len(p2) - 1
# p2l = len(p2)

# # Initialize the `spaces` dictionary for all indices
# spaces = {i: True for i in range(len(p2))}

# while right >= 0:
#     # Skip blocks with free space or already processed blocks
#     while right >= 0 and (p2[right][1] != 0 or not spaces[right]):
#         right -= 1

#     # Exit if `right` becomes invalid
#     if right < 0:
#         break

#     # Get the space needed for the current block
#     space_needed = len(p2[right][0])
#     spaces[right] = False  # Mark this block as processed

#     # Find a block with enough free space
#     for i in range(p2l):
#         if p2[i][1] != 0 and p2[i][1] >= space_needed:
#             # Move the block
#             for j in range(len(p2[right][0])):
#                 print(f"Moving element from block {right} to block {i}")
#                 p2[i][0][j + p2[i][2]] = p2[right][0][j]  # Place elements in free space

#             # Update free space counts
#             p2[i][1] -= space_needed
#             p2[i][2] += space_needed
#             p2[right][1] = space_needed
#             p2[right][0] = ["."] * space_needed

#             # Mark the source block as processed
#             spaces[right] = True
#             break

#     # Move to the next block
#     right -= 1

# print(p2)


import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc


def pr(s):
    print(s)
    pc.copy(s)


sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv) >= 2 else "../../../inputs/input9"
p1 = 0
p2 = 0
D = open(infile).read().strip()


def solve(part2):
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    for i, c in enumerate(D):
        if i % 2 == 0:
            if part2:
                A.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1

    for pos, sz, file_id in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f"{FINAL[pos+i]=}"
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break

    ans = 0
    for i, c in enumerate(FINAL):
        if c is not None:
            ans += i * c
    return ans


p1 = solve(False)
p2 = solve(True)
pr(p1)
pr(p2)
