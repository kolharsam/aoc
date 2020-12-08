file_inp = open('8.in', 'r')
lines = file_inp.read().split("\n")

insts = [x.split()[0].strip() for x in lines]
codes = [int(x.split()[1].strip()) for x in lines]

def run(insts, codes):
  i = 0
  ran = set()
  acc = 0
  while True:
      # Part 1
      if i in ran:
          return (False, acc)
      # Part 2
      elif i == len(lines):
          return (True, acc)
      ran.add(i)
      inst = insts[i]
      value = codes[i]
      if inst == 'acc':
          acc += value
      if inst == 'jmp':
          i += value
      else:
        # nop or acc
          i += 1


# Part 1
_, acc = run(insts, codes)
print(acc)

# Part 2
to_change = [idx for idx, x in enumerate(insts) if x in ('nop', 'jmp')]
for i in to_change:
  new_insts = list(insts)
  if insts[i] == 'nop':
    new_insts[i] = 'jmp'
  else:
    new_insts[i] = 'nop'
  no_trip, acc = run(new_insts, codes)
  if no_trip:
      break

print(acc)
