import sys
import re
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv)>1 else '5.in'
data = open(infile).read().strip().split('\n')

#                 [V]     [C]     [M]
# [V]     [J]     [N]     [H]     [V]
# [R] [F] [N]     [W]     [Z]     [N]
# [H] [R] [D]     [Q] [M] [L]     [B]
# [B] [C] [H] [V] [R] [C] [G]     [R]
# [G] [G] [F] [S] [D] [H] [B] [R] [S]
# [D] [N] [S] [D] [H] [G] [J] [J] [G]
# [W] [J] [L] [J] [S] [P] [F] [S] [L]
#  1   2   3   4   5   6   7   8   9

sample_stacks = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
data_stacks = [
    ['V', 'R', 'H', 'B', 'G', 'D', 'W'],
    ['F', 'R', 'C', 'G', 'N', 'J'],
    ['J', 'N', 'D', 'H', 'F', 'S', 'L'],
    ['V', 'S', 'D', 'J'],
    ['V', 'N', 'W', 'Q', 'R', 'D', 'H', 'S'],
    ['M', 'C', 'H', 'G', 'P'],
    ['C', 'H', 'Z', 'L', 'G', 'B', 'J', 'F'],
    ['R', 'J', 'S'],
    ['M', 'V', 'N', 'B', 'R', 'S', 'G', 'L']
]

stack = deepcopy(data_stacks if infile == '5.in' else sample_stacks)
stack2 = deepcopy(data_stacks if infile == '5.in' else sample_stacks)

def makeMove(moveQty, fromStack, toStack):
    while moveQty > 0:
        stack[toStack-1].insert(0, stack[fromStack-1][0])
        stack[fromStack-1].pop(0)
        moveQty-=1

def makeMove2(moveQty, fromStack, toStack):
    mvList = []
    while moveQty > 0:
        mvList.append(stack2[fromStack-1].pop(0))
        moveQty-=1
    mvList.extend(stack2[toStack-1])
    stack2[toStack-1] = mvList

for line in data:
    [mvQty, fromStack, toStack] = list(map(int, re.findall(r'\d+', line)))
    makeMove(mvQty, fromStack, toStack)
    makeMove2(mvQty, fromStack, toStack)

# part 1
ans = ''
ans2 = ''
for s in stack:
    ans += s[0]
print(ans)

# part 2
for s in stack2:
    ans2 += s[0]
print(ans2)
