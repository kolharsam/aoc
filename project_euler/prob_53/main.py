one_mil = 1_000_000

from math import comb

count = 0

for i in range(1,101):
  for j in range(0,i+1):
    if i >= j and comb(i, j) >= one_mil:
      count+=1

print(count)
