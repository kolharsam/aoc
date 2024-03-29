import sys
from collections import defaultdict, deque

E = defaultdict(list)
for line in open(sys.argv[1]):
  a, b = line.strip().split('-')
  E[a].append(b)
  E[b].append(a)

def solve(p1=True):
  start = ('start', set(['start']), None)
  ans = 0
  Q = deque([start])
  while Q:
    pos, small, twice = Q.popleft()
    if pos == 'end':
      ans += 1
      continue
    for y in E[pos]:
      if y not in small:
        new_small = set(small)
        if y.lower() == y:
          new_small.add(y)
        Q.append((y, new_small, twice))
      elif y in small and twice is None and y not in ['start', 'end'] and not p1:
        Q.append((y, small, y))
  return ans

print(solve())
print(solve(False))
