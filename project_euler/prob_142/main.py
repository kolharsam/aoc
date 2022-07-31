import math
from itertools import product
import sympy

sympy.ntheory.factorint

ns = list(range(1, 5000))
cache = {}

def isSq(n: int) -> bool:
  if n <= 0:
    return False
  if n in cache:
    return cache[n]
  else:
    res = n == math.isqrt(n) ** 2
    cache[n] = res
    return res

for (a, b, c) in product(ns, ns, ns):
  #  x + y, x − y, x + z, x − z, y + z, y − z
  if a > b > c and isSq(a+b) and isSq(a-b) and isSq(a+c) and isSq(a-c) and isSq(b+c) and isSq(b-c):
    print(a+b+c, a, b, c)
    break

# TODO: solve the equations and see if I can salvage anything...
