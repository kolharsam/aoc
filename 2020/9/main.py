file_in = open('9.in', 'r')
lines = file_in.read().splitlines()

for i,v in enumerate(lines):
  lines[i] = int(v.strip())

def checkSum(parr, sum):
  for i in parr:
    if abs(i-sum) in parr:
      return False
  return True

def run(preamble):
  i = preamble
  while i < len(lines):
    num = lines[i]
    if checkSum(lines[i-preamble:i], num):
      return num
    i+=1
  
# part 1
num = run(25)
print(num) 

# part 2
for i in range(2,len(lines)):
  p = 0
  while p < len(lines):
    l = lines.copy()[p:p+i]
    if sum(l) == num:
      print(l)
      l.sort()
      print(l[0]+l[-1])
      break
    p+=1
  