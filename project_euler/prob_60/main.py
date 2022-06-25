from itertools import combinations
from re import T

def isPrime(n):
  if n <= 1 or n % 1 > 0:
    return False
  for i in range(2, n//2):
    if n % i == 0:
      return False
  return True

ps = []

for i in range(2, 1000000):
  if isPrime(i):
    ps.append(i)

pc = {}

def checkForComboPrimes(l):
  for (x, y) in combinations(l, 2):
    sx = str(x)
    sy = str(y)
    sxsy = sx + sy
    sysx = sy + sx
    if (x, y) in pc:
      if pc[(x,y)]:
        continue
      else:
        return False
    else: 
      if not (isPrime(int(sxsy)) and isPrime(int(sysx))):
        pc[(x,y)] = False
        pc[(y,x)] = False
        return False
      else:
        pc[(x,y)] = True
        pc[(y,x)] = True
  return True

ps.reverse()

for (a,b,c,d,e) in combinations(ps, 5):
  # print("Checking: ", a, b, c, d, e)
  if checkForComboPrimes([a,b,c,d,e]):
    print(a+b+c+d+e, [a, b, c, d, e])
