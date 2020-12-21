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
inv_found_map = {}
no_match = {}

for k in aller_map.keys():
  v = aller_map[k]
  if len(v) == 1:
    found_map[v[0]] = k
    inv_found_map[k] = v[0]
  else:
    no_match[k] = v

while True:
  ch = False

  for k in no_match.keys():
    for i in no_match[k]:
      if i in found_map:
        no_match[k].remove(i)
  
  for k in no_match.keys():
    v = no_match[k]
    if len(v) == 1:
      ch = True
      found_map[v[0]] = k
      inv_found_map[k] = v[0]

  if not ch:
    break

# part 1
s = 0
for k in ingres_apps.keys():
  if k not in found_map:
    s += ingres_apps[k]

print(s)

# part 2 (sort the map lexicographically)
m = sorted(list(inv_found_map.keys()))
res = []
for i in m:
  res.append(str(inv_found_map[i]))

print(','.join(res))
