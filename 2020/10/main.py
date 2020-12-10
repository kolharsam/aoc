file_in = open('10.in', 'r')
lines = file_in.read().splitlines()

for i,v in enumerate(lines):
  lines[i] = int(v.strip())

hi = max(lines)
i = 0
onediff = 0
threediff = 0
while i != hi:
  if i + 1 in lines:
    i += 1
    onediff += 1
    continue
  if i + 2 in lines:
    i += 2
    continue
  if i + 3 in lines:
    i += 3
    threediff += 1
    continue

# part 1
print(onediff * (threediff+1))

# part 2

lines.append(0)
lines.append(hi+3)
lines.sort()

combo_map = {}
def combos(c):
  if c == len(lines)-1:
    return 1
  if c in combo_map:
    return combo_map[c]
  ans = 0
  for j in range(c+1, len(lines)):
    if lines[j]-lines[c] <= 3:
      ans += combos(j)
  combo_map[c] = ans
  return ans

print(combos(0))
    