inputFile = [line.rstrip("\n") for line in open("input")]

ROWS = 6
COLS = 50
GRID = []

for i in range(ROWS):
  temp = []
  for j in range(COLS):
    temp.append(".")

  GRID.append(temp)

def rect(a, b):
  for i in range(b):
    for j in range(a):
      GRID[i][j] = "#"

def rotateY(row, times):
  currentRow = GRID[row]
  newArr = []
  
  for i in range(COLS):
    newArr.append(".")
  
  for i in range(COLS):
    newIndex = (i + times) % COLS
    newArr[newIndex] = currentRow[i]

  GRID[row] = newArr

def rotateX(col, times):
  newRow = []
  for i in range(ROWS):
    newRow.append(".")
  
  for i in range(ROWS):
    newIndex = (i + times) % ROWS
    newRow[newIndex] = GRID[i][col]

  for i in range(ROWS):
    GRID[i][col] = newRow[i]

def countON():
  counter = 0
  for i in range(ROWS):
    for j in range(COLS):
      if GRID[i][j] == "#":
        counter += 1
  
  print(counter)

for commandline in inputFile:
  command_split = commandline.split(" ")
  command = command_split[0]

  if command == "rect":
    rectx, recty = command_split[1].split("x")
    rect(int(rectx), int(recty))
  elif command == "rotate":
    times = int(command_split[-1])
    direction = command_split[1]
    rowCol = command_split[2]

    if direction == "row":
      d, num = rowCol.split("=")
      rotateY(int(num), times)
    elif direction == "column":
      d, num = rowCol.split("=")
      rotateX(int(num), times)

for i in range(ROWS):
  print(''.join(GRID[i]))

countON()
