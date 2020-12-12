file_inp = open("12.in", "r")
lines = file_inp.read().splitlines()

# this is the dumbest way to do this
def turn(curr_dir, turn_dir, deg):
  if deg == 180:
    if curr_dir == 'E':
      return 'W'
    if curr_dir == 'S':
      return 'N'
    if curr_dir == 'W':
      return 'E'
    if curr_dir == 'N':
      return 'S'
  elif turn_dir == 'R':
    if deg == 90:
      if curr_dir == 'E':
        return 'S'
      if curr_dir == 'S':
        return 'W'
      if curr_dir == 'W':
        return 'N'
      if curr_dir == 'N':
        return 'E'
    if deg == 270:
      if curr_dir == 'E':
        return 'N'
      if curr_dir == 'S':
        return 'E'
      if curr_dir == 'W':
        return 'S'
      if curr_dir == 'N':
        return 'W'
  elif turn_dir == 'L':
    if deg == 90:
      if curr_dir == 'E':
        return 'N'
      if curr_dir == 'S':
        return 'E'
      if curr_dir == 'W':
        return 'S'
      if curr_dir == 'N':
        return 'W'
    if deg == 270:
      if curr_dir == 'E':
        return 'S'
      if curr_dir == 'S':
        return 'W'
      if curr_dir == 'W':
        return 'N'
      if curr_dir == 'N':
        return 'E'

loc = (0,0)
curr_dir = 'E'
for line in lines:
  direc = line[0]
  num = int(line[1:])
  if direc == 'F':
    if curr_dir == 'E':
      loc = (loc[0]+num, loc[1])
      continue
    if curr_dir == 'W':
      loc = (loc[0]-num, loc[1])
      continue
    if curr_dir == 'N':
      loc = (loc[0], loc[1]+num)
      continue
    if curr_dir == 'S':
      loc = (loc[0], loc[1]-num)
      continue
  if direc == 'N':
    loc = (loc[0], loc[1]+num)
    continue
  if direc == 'S':
    loc = (loc[0], loc[1]-num)
    continue
  if direc == 'W':
    loc = (loc[0]-num, loc[1])
    continue
  if direc == 'E':
    loc = (loc[0]+num, loc[1])
    continue
  if direc == 'L':
    curr_dir = turn(curr_dir, direc, num)
    continue
  if direc == 'R':
    curr_dir = turn(curr_dir, direc, num)
    continue

# part 1
print(abs(loc[0])+abs(loc[1]))

# part 2 (a cleaner and better approach)

wx = 10
wy = 1

DX = [0,1,0,-1]
DY = [1,0,-1,0]
x = 0
y = 0
dir_ = 1

for line in lines:
  direc = line[0]
  num = int(line[1:])
  if direc == 'N':
    wy += num
  elif direc == 'S':
    wy -= num
  elif direc == 'E':
    wx += num
  elif direc == 'W':
    wx -= num
  elif direc == 'L':
    for _ in range(int(num/90)):
      wx, wy = -wy, wx
  elif direc == 'R':
    for _ in range((int(num/90))):
      wx, wy = wy, -wx
  elif direc == 'F':
    x += num*wx
    y += num*wy
  else:
    assert False
    
print(abs(x)+abs(y))
