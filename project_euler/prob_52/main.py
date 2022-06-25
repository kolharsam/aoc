def containSameDigits(n):
  s = str(n)
  s2 = str(n*2)
  s3 = str(n*3)
  s4 = str(n*4)
  s5 = str(n*5)
  s6 = str(n*6)

  set1 = set(s)
  set2 = set(s2)
  set3 = set(s3)
  set4 = set(s4)
  set5 = set(s5)
  set6 = set(s6)

  if (set1.__len__() == set2.__len__() == set3.__len__() == set4.__len__() == set5.__len__() == set6.__len__()) and (set1 == set2 == set3 == set4 == set5 == set6):
    return True
  return False

for i in range(100000, 10000000):
  if containSameDigits(i):
    print(i)
    break
