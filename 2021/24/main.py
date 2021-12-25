import functools
import sys

sys.setrecursionlimit(10**7)

lines = [line.strip() for line in sys.stdin.readlines()]
ops = [line.split() for line in lines]
# print(ops)

@functools.lru_cache(maxsize=None)
def search(op_index, w_reg, x_reg, y_reg, z_reg):
  if z_reg > 10**7:
    return (False, '')
  
  if op_index >= len(ops):
    return (z_reg == 0, '')
  
  values = {'w': w_reg, 'x': x_reg, 'y': y_reg, 'z': z_reg}
  # print(values)

  def evall(var):
    return values[var] if var in values else int(var)
  
  op = ops[op_index]

  if op[0] == 'inp':
    # for d in range (9,0,-1): # for p1 
    for d in range(1,10): # for p2
      values[op[1]] = d
      result = search(op_index+1, values['w'], values['x'], values['y'], values['z'])

      if result[0]:
        print(op_index, w_reg, x_reg, y_reg, z_reg, str(d) + result[1])
        return (True, str(d) + result[1])

    return (False, 0)
  
  second = evall(op[2])

  if op[0] == 'add':
    values[op[1]] += second
  elif op[0] == 'mul':
    values[op[1]] *= second
  elif op[0] == 'div':
    if second==0:
      return (False, 0)
    values[op[1]] = int(values[op[1]] / second)
  elif op[0] == 'mod':
    if values[op[1]] < 0 or second <= 0:
      return (False, 0)
    values[op[1]] %= second
  elif op[0] == 'eql':
    values[op[1]] = 1 if values[op[1]] == second else 0
  else:
    assert False
  
  return search(op_index+1, values['w'], values['x'], values['y'], values['z'])

print(search(0,0,0,0,0))
