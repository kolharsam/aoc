input = [int(x) for x in "4329 385 0 1444386 600463 19 1 56615".split(" ")]
example = [125, 17]

"""
0 -> 1
even digits -> 2 stones [left half, right half]
none -> multiply by 2024
"""


# def proc_stone(stone):
#     str_stone = str(stone)
#     len_stone = len(str_stone)
#     if stone == 0:
#         return [1]
#     if len_stone % 2 == 0:
#         return [int(str_stone[: len_stone // 2]), int(str_stone[len_stone // 2 :])]
#     return [stone * 2024]


# res = input.copy()
# cache = {}
# # tot = 0
# # cache_tot = 0
# for i in range(75):
#     new_res = []
#     for elem in res:
#         # tot += 1
#         if elem in cache:
#             # cache_tot += 1
#             new_res.extend(cache[elem])
#             continue
#         cache[elem] = proc_stone(elem)
#         new_res.extend(cache[elem])
#     res = new_res
#     print("completed iteration", i + 1)

# print(len(res))


DP = {}


def solve(x, t):
    """If we put [x] through [t] steps, how long is the resulting list?"""
    if (x, t) in DP:
        return DP[(x, t)]
    if t == 0:
        ret = 1
    elif x == 0:
        ret = solve(1, t - 1)
    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left = dstr[: len(dstr) // 2]
        right = dstr[len(dstr) // 2 :]
        left, right = (int(left), int(right))
        ret = solve(left, t - 1) + solve(right, t - 1)
    else:
        ret = solve(x * 2024, t - 1)
    DP[(x, t)] = ret
    return ret


def solve_all(t):
    return sum(solve(x, t) for x in input)


print(solve_all(25))
print(solve_all(75))
