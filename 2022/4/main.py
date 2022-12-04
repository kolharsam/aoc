import sys

infile = sys.argv[1] if len(sys.argv)>1 else '4.in'
data = open(infile).read().strip().split('\n')

c = 0

def makeList(x, y):
    if x == y:
        return [x]
    
    if x < y:
        return list(range(x, y+1))
    
    return list(range(y, x+1))

def contain(a, b, x, y):
    p1 = set(makeList(a, b))
    p2 = set(makeList(x, y))
    
    # return bool(p1 & p2)  # for part 2
    return p1.issuperset(p2) or p2.issuperset(p1) # part 1

for line in data:
    [e1, e2] = line.split(',')
    [p1e1, p2e1] = e1.split('-')
    [p1e2, p2e2] = e2.split('-')
    
    if contain(int(p1e1), int(p2e1), int(p1e2), int(p2e2)):
        c += 1

# part 1 & 2
print(c)
