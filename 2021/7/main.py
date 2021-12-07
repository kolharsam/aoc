import statistics
import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()[0].split(',')

nums = list(map(int, lines))

fuelD = int(statistics.median(nums))
f2 = statistics.mean(nums).__round__(1).__int__()

print(f2)

c = 0
for i in nums:
  c += abs(fuelD - i)

print(c)

def sumN(n):
  return int((n * (n + 1)) / 2)

c2 = 0
for i in nums:
  a = abs(f2 - i)
  c2 += sumN(a)

print(c2)
