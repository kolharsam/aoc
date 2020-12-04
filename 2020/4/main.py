import fileinput
import re

ans = 0
passport = {}
# needed for part 2
passports = []

for line in fileinput.input():
  line = line.strip()
  if not line:
    passports.append(passport)
    valid = True
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
      if field not in passport:
        valid = False
    # print(passport, valid)
    if valid:
      ans += 1
    passport = {}
  else:
    words = line.split()
    for word in words:
      k,v = word.split(':')
      passport[k] = v

# part 1
print(ans)

def is_valid_passport(passport):
  try:
      byr = int(passport['byr'])
      if not 1920 <= byr <= 2002:
          return False
      iyr = int(passport['iyr'])
      if not 2010 <= iyr <= 2020:
          return False
      eyr = int(passport['eyr'])
      if not 2020 <= eyr <= 2030:
          return False
      hgt = passport['hgt']
      # I got the idea to do this very late
      # my first soln, was a .split() based one
      match = re.match(r'(\d+)(cm|in)', hgt)
      height, unit = match[1], match[2]
      i_hgt = int(height)
      if unit == 'cm':
          if not 150 <= i_hgt <= 193:
              return False
      elif unit == 'in':
          if not 59 <= i_hgt <= 76:
              return False
      else:
          return False
      hcl = passport['hcl']
      if hcl[0] != '#' or len(hcl) != 7:
          return False
      ecl = passport['ecl']
      if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
          return False
      pid = passport['pid']
      if not pid.isdigit() or len(pid) != 9:
          return False
      return True
  except:
      return False

# part 2
p2 = 0
for i in passports:
  if is_valid_passport(i):
    p2 += 1

print(p2)
