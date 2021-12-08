import sys

with open(sys.argv[1]) as f:
  lines = list(map(str.split, f.readlines()))

# part 1 - find how many are 1,4,7 or 8
strs = 0
for line in lines:
  sp = line[11:]
  for s in sp:
    if len(s) in [2,3,4,7]:
      strs += 1

print(strs)

# part 2 - sum of the decoded numbers
s = 0
for line in lines:
  p1 = line[:10]
  p2 = line[11:]
  
  num_map = {}
  for i in p1:
    lp = len(i)
    if lp == 2:
      num_map[i] = 1
    elif lp == 3:
      num_map[i] = 7
    elif lp == 4:
      num_map[i] = 4
    elif lp == 7:
      num_map[i] = 8
    elif lp == 5:
      num_map[i] = 3 # NO! 
    elif lp == 6:
      num_map[i] = 5 # no!
  print(num_map)

  s += int(''.join(list(map(lambda x : str(num_map[x]), p2))))

print(s)

"""/*

  const three = pattern.find(item => item.length === 5 && one.split('').every(ele => item.includes(ele)))
  const nine = pattern.find(item => item.length === 6 && four.split('').every(ele => item.includes(ele)))
  const e = eight.split('').find(ele => !nine.includes(ele))
  const zero = pattern.find(item => item.length === 6 && item !== nine && one.split('').every(ele => item.includes(ele)))
  const six = pattern.find(item => item.length === 6 && item !== nine && item !== zero)
  const two = pattern.find(item => item.length === 5 && item !== three && item.includes(e))
  const five = pattern.find(item => item.length === 5 && item !== three && !item.includes(e))


*/"""
