file_in = open("in", "r")
file = file_in.read().split("\n")

currentSetOfQs = set()
total_c = 0
total_c2 = 0
common_set = []

def get_intersection(s):
  st = s[0]
  for i in s[1:]:
    st = st & i
  return st

for i in file:
  if not i:
    total_c += len(currentSetOfQs)
    total_c2 += len(get_intersection(common_set))
    currentSetOfQs = set()
    common_set = []
  else:
    common_set.append(set([c for c in i]))
    for j in i:
      currentSetOfQs.add(j)

# p1
print(total_c+len(currentSetOfQs))

# p2
print(total_c2+len(currentSetOfQs))

