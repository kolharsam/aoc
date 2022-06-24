from itertools import product
from math import sqrt

def isPrime(n):
  if n == 1:
    return False
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def goldbachConjecture(num):
  for (x,y) in list(product(range(1, num-1), range(1,int(sqrt(num))))):
    if not isPrime(x):
      continue
    if (x + 2*pow(y, 2)) == num:
      return (x,y)
  return (-1,-1)

for i in range(3, 6000, 2):
  if isPrime(i):
    continue
  if goldbachConjecture(i) == (-1, -1):
    print(i)
    break
