from math import factorial

def isCurious(n):
  s = 0
  for i in str(n):
    s += factorial(int(i))
  return s == n

l = []

for i in range(3, 10000000):
  if isCurious(i):
    l.append(i)

print(sum(l), l)
