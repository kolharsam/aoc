file_in = open("in", "r")
file = file_in.read().strip().split('\n')[0]

M = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'

for c in alpha:
  M[c.lower()] = c.upper()
  M[c.upper()] = c.lower()

ans = 1e5
for i in alpha:
  st2 = [a for a in file if a != i.lower() and a != i.upper()]
  stack = []
  for c in st2:
    if stack and c == M[stack[-1]]:
      stack.pop()
    else:
      stack.append(c)
  ans = min(ans, len(stack))

# part 2
print(ans)

