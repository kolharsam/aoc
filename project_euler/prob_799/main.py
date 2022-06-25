from itertools import combinations
import operator

# Pentagonal Puzzle

def mkPentagonNum(num):
  return int((num*((3*num)-1))/2)

ps = []

for i in range(1, 15000):
  ps.append(mkPentagonNum(i))

pc = {}

for (x, y) in combinations(ps, 2):
  s = x+y
  if s in ps:
    if s not in pc:
      pc[s] = 1
    else:
      pc[s] += 1
      if pc[s] >= 100:
        print(s)
        break
