from itertools import product

def mkPentagonNum(num):
  return int((num*((3*num)-1))/2)

ps = []

for i in range(1000, 10000):
  ps.append(mkPentagonNum(i))

for (i, j) in list(product(ps, ps)):
  if (i+j) in ps and abs(j - i) in ps:
    print(i,j,i+j,i-j)
