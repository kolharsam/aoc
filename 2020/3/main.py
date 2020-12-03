file_inp = open("input", "r")
lines = file_inp.read().split('\n')

rows = []
for i in lines:
    row = [j for j in i]
    rows.append(row)

maxy = len(rows)
maxx = len(rows[0])

def get_tree_count(jx, jy):
  currx = 0
  curry = 0
  count = 0
  for i in range(maxy-1):
    currx += jx
    curry += jy
    if currx >= maxx:
      currx = 0 + (currx % maxx)
    if curry < maxy and rows[curry][currx] == '#':
      count += 1
  return count

# part 1
print(get_tree_count(3, 1))

# part 2
print(get_tree_count(1,1) * get_tree_count(3,1) * get_tree_count(5,1) * get_tree_count(7,1) * get_tree_count(1,2))

