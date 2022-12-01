import sys

infile = sys.argv[1] if len(sys.argv)>1 else '1.in'
data = open(infile).read().strip().split('\n')

cals = []
cal = []

for line in data:
    if line == '':
        cals.append(cal)
        cal = []
    else:
        cal.append(int(line))

# part 1
l = list(map(sum, cals))
print(max(l))

# part 2
l.sort(reverse=True)
print(sum(l[0:3]))
