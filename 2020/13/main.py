import math

file_inp = open("13.in", "r")
lines = file_inp.read().splitlines()

my_time = int(lines[0])
schedule =[int(x) for x in lines[1].split(",") if x != 'x']
p2_schedule = [(idx, int(x)) for idx, x in enumerate(lines[1].split(',')) if x != 'x']

near_map = {}

for x in schedule:
  i = x
  while i <= my_time:
    i += x
  near_map[x] = i
  
sm_diff = math.inf
bus = 0
for k, v in near_map.items():
  diff = v - my_time 
  if diff < sm_diff:
    sm_diff = diff
    bus = k

# part 1
print(sm_diff*bus)

# print(p2_schedule)

# there are 2 nice ways of doing this.(that I am aware of)
# 1) By using the Chinese Remainder Theorem
# 2) By using the Euclidean Algorithm (as used in here)

min_val = 0
pr = 1
for i in p2_schedule:
  while (min_val + i[0]) % i[1] != 0:
    min_val += pr
  pr *= i[1]
  
print(pr)
