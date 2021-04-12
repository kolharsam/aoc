from itertools import combinations, count
from numpy import product

inp = open('input', 'r').readlines()

ws = [int(x) for x in inp]

# qes = []
# for i in set_partitions(ws, 3):
#     a, b, c = i
#     if sum(list(a)) == sum(list(b)) == sum(list(c)):
#         t = (i, product(list(a)), len(list(a)))
#         # print(t)
#         qes.append(t)

# sorted(qes, key=(lambda x: x[2]))

def solve(part_one):
    s = sum(ws)
    target = s // 3 if part_one else s // 4
    for i in count():
        c = combinations(ws, i)
        m = float('inf')
        for g1 in c:
            if sum(g1) != target:
                continue
            m = min(m, product(g1))
        if m < float('inf'):
            return m

# part 1
# print(qes[0], qes[0][1])
print(solve(True))
# part 2
print(solve(False))
