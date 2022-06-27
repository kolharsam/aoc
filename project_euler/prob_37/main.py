# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work 
# from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from sympy import isprime, sieve

tns = []

def isTruncatableFromLeft(n):
  s = [x for x in str(n)]
  while not s.__len__() == 0:
    if not isprime(int(''.join(s))):
      return False
    s.pop(0)
  return True

def isTruncatableFromRight(n):
  s = [x for x in str(n)]
  while not s.__len__() == 0:
    if not isprime(int(''.join(s))):
      return False
    s.pop()
  return True

def isTruncatable(n):
  return isTruncatableFromLeft(n) and isTruncatableFromRight(n)

for i in sieve.primerange(1000000):
  if i not in [2,3,5,7] and isTruncatable(i):
    tns.append(i)

print(tns, sum(tns))
