from sympy import divisor_count

tns = []
s = 0

for i in range(1, 100000):
  s += i
  tns.append(s)

for i in tns:
  d = divisor_count(i)
  if d >= 500:
    print(i)
    break
