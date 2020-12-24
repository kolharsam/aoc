from copy import copy, deepcopy
from collections import deque

sampleInput = [3, 8, 9, 1, 2, 5, 4, 6, 7]
probInput = [9, 7, 4, 6, 1, 8, 3, 5, 2]

def rotate_right(l):
  lq = deque(deepcopy(l))
  lq.rotate()
  return list(lq)

def insert_at(l,pos,ins):
  l1 = list(l[:pos+1])
  l1.extend(ins)
  l1.extend(l[pos+1:])
  return l1

def playround(lis, point):
  befCurr = lis[:point]
  curr = lis[point]
  sta = ((point+1)%len(lis))
  stb = ((point+4)%len(lis))
  sub = []
  if sta < stb:
    sub = lis[sta:stb]
  else:
    t = [lis[sta]]
    sta+=1
    while len(t) != 3:
      if sta >= len(lis):
        sta = sta % len(lis)
      t.append(lis[sta])
      sta+=1
    sub = t

  rest = lis[stb:]
  
  addrest = True
  for i in rest:
    if i in befCurr:
      addrest = False
      break
  
  rest = rest if addrest else []
  
  befCurr = [x for x in befCurr if x not in sub]
  
  curr_list = befCurr
  curr_list.extend([curr])
  curr_list.extend(rest)
  
  dest_num = curr - 1
  # print("in:", lis, point, lis[point], sub, ((point+1)%len(lis)), ((point+4)%len(lis)), dest_num, rest, befCurr)
  
  if dest_num in sub or dest_num == 0:
    d = copy(dest_num)-1
    while True:
      if d <= 0:
        d = len(lis)
      if d not in sub and d != curr:
        dest_num = d
        break
      d-=1 
  
  di = curr_list.index(dest_num)
  
  curr_list = insert_at(curr_list, di, sub)

  if curr_list[point] == lis[point]:
    # print("out", curr_list)
    return curr_list
  
  while curr_list[point] != lis[point]:
    curr_list = rotate_right(curr_list)
  
  # print("out", curr_list)
  
  return curr_list

n = 0
point = 0
l = deepcopy(probInput)
while True:
  if n == 100:
    break
  
  l = playround(deepcopy(l), copy(point))
  # print(l)
  
  point+=1
  n+=1
  if point >= len(l):
    point = point % len(l)
  
# part 1
print(l)


modInp = deepcopy(sampleInput)

for i in range(10, 1000001):
  modInp.append(i)

n = 0
point = 0
l = copy(modInp)
while True:
  if n == 100:
    break
  
  l = playround(l, point)
  
  point+=1
  n+=1
  print(n)
  if point >= len(l):
    point = point % len(l)

pos1 = l.index(1)
# part 2
print(l[pos1-1]*l[pos1+1])
