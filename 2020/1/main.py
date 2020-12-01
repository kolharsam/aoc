file = open("input", "r")
fileInput = file.read().split("\n")
ch = []

for i in fileInput:
  ch.append(int(i))

# part 1
for i in ch:
  if i in ch and (2020-i) in ch:
    print((i, (2020-i)))

# part 2
for i in ch:
  for j in ch:
    for k in ch:
      if i + j + k == 2020:
        print(i,j,k)

# since this is unique, it should be done in a better way
