import sys
from collections import deque, namedtuple

GRID = []
for line in open('input2').readlines():
    GRID.append(list(line.strip()))

R = len(GRID)
C = len(GRID[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]

Q = deque()
State = namedtuple('State', ['r', 'c', 'keys', 'd'])
all_keys = set()

for r in range(R):
    for c in range(C):
        if GRID[r][c] == '@':
            Q.append(State(r,c, set(), 0))
        if 'a' <= GRID[r][c] <= 'z':
            all_keys.add(GRID[r][c])

print(len(all_keys), all_keys)

SEEN = set()
while Q:
    S = Q.popleft()
    key = (S.r, S.c, tuple(sorted(S.keys)))

    if key in SEEN:
        continue
    SEEN.add(key)
    if len(SEEN)%100000 == 0:
        print(len(SEEN))
    if not (0<=S.r < R and 0<=S.c<C and GRID[S.r][S.c]!='#'):
        continue
    if 'A'<=GRID[S.r][S.c]<='Z' and GRID[S.r][S.c].lower() not in S.keys:
        continue
    newkeys = set(S.keys)
    if 'a' <= GRID[S.r][S.c] <= 'z':
        newkeys.add(GRID[S.r][S.c])
        if newkeys == all_keys:
            print(S.d)
            sys.exit(0)
    for d in range(4):
        rr,cc = S.r+DR[d], S.c+DC[d]
        Q.append(State(rr,cc, newkeys, S.d+1))
     