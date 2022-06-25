# Champernowne's constant

ch = 1000000
indexes = [
  1,
  10,
  100,
  1000,
  10000,
  100000,
  ch
]

st = ""

for i in range(1, ch):
  st += str(i)

d = 1

for (idx,i) in enumerate(st):
  if idx+1 > ch:
    break
  if idx+1 in indexes:
    d *= int(i)

print(d)
