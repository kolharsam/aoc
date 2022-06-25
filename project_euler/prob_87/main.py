from itertools import product
import math

def isPrime(n):
  if n == 1:
    return False
  for i in range(2, n):
    if (n%i) == 0:
      return False
  return True

ps = []

for i in range(2, int(math.sqrt(50000000))):
  if isPrime(i):
    ps.append(i)

ns = []

for (a, b, c) in product(ps, ps, ps):
  ns.append(((a**2) + (b**3) + (c**4), (a,b,c)))

c = 0

for i in ns:
  s = i[0]
  # (a,b,c) = i[1]
  if s <= 50000000:
    c+=1

print(c)
