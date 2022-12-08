import sys

infile = sys.argv[1] if len(sys.argv)>1 else '8.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
trees = [list(x) for x in lines]

rl = len(lines)
cl = len(lines[0])

vis = 0

def isVisibleFromTop(r,c):
    n = 0
    for i in range(r):
        if trees[i][c] >= trees[r][c]:
            return False, n+1
        n+=1
    return True,n

def isVisibleFromBottom(r,c):
    n = 0
    for i in range(rl-1, r, -1):
        if trees[i][c] >= trees[r][c]:
            return False, n+1
        n+=1
    return True, n

def isVisibleFromLeft(r,c):
    n = 0
    for i in range(c):
        if trees[r][i] >= trees[r][c]:
            return False, n+1
        n+=1
    return True, n

def isVisibleFromRight(r,c):
    n = 0
    for i in range(c+1, cl):
        if trees[r][i] >= trees[r][c]:
            return False, n+1
        n+=1
    return True, n

max_score = 0

for r in range(rl):
    for c in range(cl):
        if r == 0 or r == rl-1 or c == 0 or c == cl-1:
            vis += 1
            continue
        vt, ct = isVisibleFromTop(r,c)
        vb, cb = isVisibleFromBottom(r,c)
        vle, cle = isVisibleFromLeft(r,c)
        vlr, clr = isVisibleFromRight(r,c)
        if vt or vb or vle or vlr:
            vsc = ct * cb * cle * clr
            vis += 1
            max_score = max(vsc, max_score)

print(vis) # part 1
print(max_score) # part 2
