inp = open("21.in", "r")
inp_lines = inp.read().strip().splitlines()

aller_map = {}

# each allergen will be in atmost one ingredient
# each ingredient can may or may not contain an
# allergen

ingres_apps = {}

for l in inp_lines:
  ingre_set = set()
  aller_set = set()
  spl = l.split(" (")
  ingre = spl[0].split()
  aller = spl[1].split(")")[0].split("contains ")[1].split(", ")
  for i in ingre:
    ingre_set.add(i)
    if i in ingres_apps:
      ingres_apps[i]+=1
    else:
      ingres_apps[i] = 1
  for i in aller:
    aller_set.add(i)
    if i in aller_map:
      aller_map[i].append(ingre)
    else:
      aller_map[i] = [ingre]

for k in aller_map.keys():
  v = aller_map[k]
  if len(v) > 1:
    d = set(v[0])
    for i in v[1:]:
      d &= set(i)
    aller_map[k] = list(d)
  else:
    aller_map[k] = v[0]

found_map = {}

for k in aller_map.keys():
  v = aller_map[k]
  if len(v) == 1:
    found_map[v[0]] = k
  else:
    for i in v:
      if i not in found_map:
        found_map[i] = k

# part 1
s = 0
for k in ingres_apps.keys():
  if k not in found_map:
    s += ingres_apps[k]

print(s)

# part 2 (sort the map lexicographically)
m = sorted(list(found_map.values()))
res = []
for i in m:
  res.append(str(i))

print(','.join(res))
