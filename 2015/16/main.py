file_in = open("16.in", "r")
lines = file_in.read().splitlines()

soln = {
  'children': 3,
  'cats': 7,
  'samoyeds': 2,
  'pomeranians': 3,
  'akitas': 0,
  'vizslas': 0,
  'goldfish': 5,
  'trees': 3,
  'cars': 2,
  'perfumes': 1
}

inp = []

for line in lines:
  line = line.split()
  prop1, val1 = line[2][:-1], int(line[3][:-1])
  prop2, val2 = line[4][:-1], int(line[5][:-1])
  prop3, val3 = line[6][:-1], int(line[7])
  inp.append({prop1: val1, prop2: val2, prop3: val3})

for idx, i in enumerate(inp):
  f1 = True
  curr_keys = i.keys()
  for j in curr_keys:
    if soln[j] != i[j]:
      f1 = False
  if f1:
    # part 1
    print("p1", idx+1)
  f2 = False
  for k,v in i.items():
    if k == 'trees' or k == 'cats':
      if i[k] >= soln[k]:
        f2 = True
        break
    elif k == 'goldfish' or k == 'pomeranians':
      if i[k] <= soln[k]:
        f2 = True
        break
    elif i[k] != soln[k]:
      break
  if f2:
    print(i)
    print("p2", idx+1)
