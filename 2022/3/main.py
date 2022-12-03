import sys

infile = sys.argv[1] if len(sys.argv)>1 else '3.in'
data = open(infile).read().strip().split('\n')

def retPrio(c):
    ch = ord(c)
    if ch >= 65 and ch <= 90:
        return ch-38
    if ch >= 97 and ch <= 122:
        return ch-96

def retCommon(s1, s2):
    for s in s1:
        for r in s2:
            if r == s:
                return retPrio(s)

s = 0

for line in data:
    l = len(line)//2
    p1, p2 = line[0:l], line[l:]
    s += retCommon(p1,p2)

# part 1
print(s)

ps = []
p = 0
l = []

for line in data:
    p += 1
    l.append(line)
    if p == 3:
        p = 0
        ps.append(l)
        l = []

s = 0

def retCommon2(lll):
    for s in lll[0]:
        for r in lll[1]:
            for k in lll[2]:
                if r == s == k:
                    return retPrio(s)

for pp in ps:
    s += retCommon2(pp)

# part 2
print(s)
