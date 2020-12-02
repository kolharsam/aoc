fileInput = open("input", "r")
fileData = fileInput.read().split("\n")

splitData = []
for i in fileData:
  interm = i.split()
  lim = interm[0].split("-")
  low = int(lim[0])
  hi = int(lim[1])
  splitData.append([low, hi, interm[1][0], interm[2]])

def countOccurance(letter, word, hi, lo): 
  count = 0
  for i in word:
    if i == letter:
      count += 1
  return lo <= count and hi >= count

p1 = 0

for i in splitData:
  if countOccurance(i[2], i[3], i[1], i[0]):
    p1 += 1

print(p1)

def filter(letter, word, hi, lo):
  return (word[lo] == letter) ^ (word[hi] == letter)

p2 = 0
for i in splitData:
  if filter(i[2], i[3], i[1]-1, i[0]-1):
   p2 += 1

print(p2) 
