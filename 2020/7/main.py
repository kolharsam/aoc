from collections import deque

file_inp = open("in2", "r")
lines = file_inp.read().split("\n")

bag_map = {}

for line in lines:
  line = line.strip()
  if line:
    words = line.split()
    container = words[0]+words[1]+words[2]
    container = container[:-1]
    if words[-3] == 'no': # no other bags case
      continue
    else:
      idx = 4
      while idx < len(words):
        bag = words[idx]+words[idx+1]+words[idx+2]+words[idx+3]
        if bag.endswith('.'):
          bag = bag[:-1]
        if bag.endswith(','):
          bag = bag[:-1]
        if bag.endswith('s'):
          bag = bag[:-1]
        n = int(bag[0])
        assert bag[1] not in '0123456789'
        while any([bag.startswith(d) for d in '0123456789']):
          bag = bag[1:]
       if container not in bag_map:
          bag_map[container] = []
        # part 1
        # bag_map[container].append(bag)
        # part 2
        bag_map[container].append((n,bag))
        idx += 4

# print(bag_map)

visited = set()
Q = deque(['shinygoldbag'])
while Q:
  x = Q.popleft()
  if x in visited:
    continue
  visited.add(x)
  for (_, y) in bag_map.get(x, []):
    Q.append(y)

# p1
print(len(visited)-1)

# part 2
def get_bags_fit2(bag):
  ans = 1
  for (n, y) in bag_map.get(bag, []):
    ans += n*get_bags_fit2(y)
  return ans

print(get_bags_fit2('shinygoldbag')-1)
 
