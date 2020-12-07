from itertools import combinations

file_in = open("17.in", "r")
lines = file_in.read().splitlines()
lines = list(map(int, lines))

total = 0
combos = []
for n in range(len(lines)):
  for combo in combinations(lines, n):
    if sum(combo) == 150:
      combos.append(list(combo))
      total += 1

# part 1      
print(total)

# part 2
m = min(list(map(len, combos)))
c2 = 0
for i in combos:
  if len(i) == m:
    c2 += 1

print(c2)

for i in combos:
  print(combos)
