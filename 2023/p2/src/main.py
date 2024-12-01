import sys
D = open(sys.argv[1]).read().strip().splitlines()

ids = 0
red = 12
green = 13
blue = 14
pws = 0

for l in D:
    ll = l.split(":")
    game_no = int(ll[0].split()[1])
    games = ll[1].split(";")
    v = True
    max_r = 0
    max_g = 0
    max_b = 0
    for gs in games:
        g = gs.strip().split(", ")
       
        for ns in g:
            cls_split = ns.split()
            nss = int(cls_split[0])
            if cls_split[1] == "red":
                max_r = max(nss, max_r)
                if nss > red and v == True:
                    v = False
            elif cls_split[1] == "green":
                max_g = max(nss, max_g)
                if nss > green and v == True:
                    v = False
            elif cls_split[1] == "blue":
                max_b = max(nss, max_b)
                if nss > blue and v == True:
                    v = False

    pws += (max_g * max_b * max_r)
    if v:
        ids += game_no

print(ids) # part 1
print(pws) # part 2
