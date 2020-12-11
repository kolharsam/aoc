from copy import deepcopy

file_inp = open("11.in", "r")
lines = file_inp.read().splitlines()

# implementing the game of life(a slight variation of it)!

G = []
for line in lines:
  row = [x for x in line]
  G.append(row)
occ = '#'
floor = '.'
empty = 'L'
NG = deepcopy(G)

def countSeats(grid):
  count = 0
  for row in grid:
    for seat in row:
      if seat == occ:
        count += 1
  return count

def print_grid(grid):
  for i in grid:
    print(''.join(i))
  print()

def playGameOfLife(grid, p2):
  new_grid = deepcopy(grid)
  change = False
  while True:
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        nocc = 0
        for dr in [0,-1,1]:
          for dc in [0,-1,1]:
            if dr == 0 and dc == 0:
              continue
            rr = r + dr
            cc = c + dc
            while 0<=rr<len(grid) and 0<=cc<len(grid[0]) and grid[rr][cc] == floor and p2:
              rr = rr + dr
              cc = cc + dc
            if 0<=rr<len(grid) and 0<=cc<len(grid[0]) and grid[rr][cc] == occ:
              nocc += 1
        if grid[r][c] == empty:
          if nocc == 0:
            new_grid[r][c] = occ
            change = True
        elif grid[r][c] == occ:
          if nocc >= (5 if p2 else 4):
            new_grid[r][c] = empty
            change = True
    if not change:
      print(countSeats(new_grid))
      break
    grid = deepcopy(new_grid)
    change = False

# part 1
playGameOfLife(G, False)

# part 2
playGameOfLife(NG, True)
