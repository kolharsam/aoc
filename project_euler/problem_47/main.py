from sympy.ntheory import primefactors

nms = []

for i in range(100000, 1000000):
  pf = primefactors(i)
  if pf.__len__() == 4:
    nms.append(i)

for i in nms:
  if i+1 in nms and i+2 in nms and i+3 in nms:
    print(i, i+1, i+2, i+3)
