import sys
D = open(sys.argv[1]).read().strip().splitlines()

sc = 0
cop = {}

for l in range(len(D)):
    cop[l+1] = 1

def found(w, m):
    f = []
    for wn in w:
        for mn in m:
            if wn == mn:
                f.append(wn)
                continue
    
    return len(f)

for i, l in enumerate(D):
    lsp = l.split(" | ")
    wns = list(map(int, list(filter(lambda x:x.isdigit(), lsp[0].split(": ")[1].split(" ")))))
    mns = list(map(int, list(filter(lambda x:x.isdigit(), lsp[1].split()))))
    
    f = found(wns, mns)

    if f > 0:
        c = cop[i + 1]
        ff = f

        while c > 0:
            for ffff in range(i+2, i+f+2):
                cop[ffff]+=1
            c -= 1

        sc += 2 ** (f-1)

print(sc) # part 1
print(sum(cop.values())) # part 2
