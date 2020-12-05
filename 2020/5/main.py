file_in = open("in", "r")
lines = file_in.read().split("\n")

high = 0
seatCount = 0
seats = []

def get_divide(ran, change):
  if change == 'up':
    newran = (ran[0], int(ran[0]+((abs(ran[0]-ran[1])/2))))
    return newran
  elif change == 'down':
    newran = (int(ran[0]+((abs(ran[0]-ran[1])/2)))+1, ran[1])
    return newran

for i in lines:
  row = i[0:7]
  col = i[7:]
  ran = (0,127)
  ran2 = (0,7)
  point2 = 0
  point = 0
  for j in row[0:6]:
    if j == 'F':
      ran = get_divide(ran, 'up')
    elif j == 'B':
      ran = get_divide(ran, 'down')
  if row[-1] == 'F':
    point = ran[0]
  else:
    point = ran[1]
  for k in col[0:2]:
    if k == 'L':
      ran2 = get_divide(ran2, 'up')
    elif k == 'R':
      ran2 = get_divide(ran2, 'down')
  ifcol[-1] == 'L':
    point2 = ran2[0]
  else:
    point2 = ran2[1]
  seatID = (point*8 + point2)
  seats.append(seatID)
  # print(seatID)
  seatCount += 1
  if seatID > high:
    high = seatID

# part 1
print(high)

# part 2
for i in range(0,seatCount):
  if i not in seats:
    print(i)
 
