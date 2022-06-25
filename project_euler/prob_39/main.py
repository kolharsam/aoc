from itertools import combinations
import operator

def isRightTriangle(a, b, c):
  if ((a**2) + (b**2)) == (c**2):
    return True
  return False

n = {}

for (a,b,c) in combinations(range(1, 400), 3):
  s = a+b+c
  if a <= b and b <= c and a <= c and s <= 1000 and isRightTriangle(a, b, c):
    if s not in n:
      n[s] = 1
    else:
      n[s] += 1

print(max(n.items(), key=operator.itemgetter(1)))
