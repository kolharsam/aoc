from itertools import product

ns = list(range(1,1000))

def isTriplet(a,b,c):
  return ((a**2) + (b**2)) == (c**2)

for (a,b,c) in product(ns,ns,ns):
  if a < b < c and isTriplet(a, b, c) and ((a+b+c) == 1000):
    print(a, b, c, a*b*c)
    break
