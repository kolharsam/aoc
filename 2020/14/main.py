import math

file_inp = open("14.in", "r")
lines = file_inp.read().splitlines()

value_map = {}
value_map2 = {}
i = 0

def run(mask, bin_val):
  val = ['0' for _ in range(len(mask))]
  for id, v in enumerate(mask):
    if v != 'X':
      val[id] = v
    else:
      val[id] = bin_val[id]
  return ''.join(val)

def count_floating(mask):
  v = [x for x in mask if x == 'X']
  return len(v)

def get_combos(val, num):
  cbs = []
  combos = []
  for i in range(0, int(math.pow(2, num))):
    cbs.append(format(i, '0'+str(num)+'b'))
  for i in cbs:
    new_val = val.copy()
    curr_form = [x for x in i]
    curr_form.reverse()
    for id, v in enumerate(val):
      if v == 'X':
        new_val[id] = curr_form.pop()
    combos.append(new_val)
  return [str(int(''.join(x),2)) for x in combos]

def run2(mask, mem_addr):
  val = ['0' for _ in range(len(mask))]
  for id, v in enumerate(mask):
    if v == '0':
      val[id] = mem_addr[id]
    elif v == '1':
      val[id] = '1'
    else:
      val[id] = 'X'
  num_float = count_floating(val)
  # total number of combos would be 2^num_float
  if num_float == 0:
    return [int(''.join(val), 2)]
  return get_combos(val, num_float)

while True:
  if i >= len(lines):
    break
  if lines[i].__contains__('mask'):
    curr_mask = lines[i].split(" = ")[1]
    i+=1
    # this condition can be improved
    while (i < len(lines)) and (not lines[i].__contains__('mask')) or not lines[i]:
      mem_spl = lines[i].split(" = ")
      bin_val = format(int(mem_spl[1]), '036b')
      # a better way to do this would be regex
      mem_addr = int(mem_spl[0].split('[')[1].split(']')[0])
      ans = run(curr_mask, bin_val)
      ans2 = run2(curr_mask, format(int(mem_addr), '036b'))
      value_map[mem_addr] = int(ans, 2)
      for x in ans2:
        value_map2[x] = int(mem_spl[1])
      i+=1
      if i >= len(lines):
        break
# part 1
print("part 1:", sum(value_map.values()))
# part 2
print("part 2:", sum(value_map2.values()))
