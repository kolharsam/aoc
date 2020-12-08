from collections import defaultdict

file_in = open("14.in", 'r')
lines = file_in.read().splitlines()

inp = []
r_map = {}
# parse input
for line in lines:
  line = line.split()
  inp.append((line[0], (int(line[3]), int(line[6])), int(line[13]), 0))
  # format is (name, (speed, time), rest, points)
  r_map[line[0]] = 0

for k in r_map.keys():
  dis = 0
  t = 0
  ma = list(filter(lambda x:x[0] == k, inp))[0]
  speed, time, rest_time = ma[1][0], ma[1][1], ma[2]
  while t < 2503:
    t += time
    if t > 2503:
      dis += (2503 - t)*speed
    else:
      dis += time*speed
    t += rest_time
  r_map[k] = dis

# part 1
print(max(r_map.values()))


lines = [x.strip().split() for x in lines]

def get_distance(v, tt, tr, maxt):
  t = 0
  d = 0
  while True:
    for _ in range(tt):
      d += v
      t += 1
      if t == maxt:
        return d
    t += tr
    if t >= maxt:
      return d

points = defaultdict(int)
for t in range(1, 2504):
  best = -float('inf')
  winners = []
  for l in lines:
    distance = get_distance(int(l[3]), int(l[6]), int(l[-2]), t)
    if distance >= best:
      if distance == best:
        winners.append(l[0])
      else:
        winners = [l[0]]
      best = max(best, distance)
  for winner in winners:
    points[winner] += 1

print(max(points.values()))
