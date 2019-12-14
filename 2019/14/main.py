from copy import deepcopy

def p1(s):
    n, item = s.split()
    return int(n), item

ALL_IN = {}
F = {}

for line in open('input').readlines():
    line = line.strip()
    need, get = line.split(" => ")
    numget, get = p1(get)
    need = need.split(", ")
    need = [p1(s.strip()) for s in need]
    for (n, y) in need:
        if y not in ALL_IN:
            ALL_IN[y] = 0
        ALL_IN[y] += 1
    assert get not in F
    F[get] = (numget, need)

def cost(net_fuel):
    IN = deepcopy(ALL_IN)
    IN['FUEL'] = 0
    REQ = {'FUEL' : net_fuel}
    # amount_req = 0
    done = False

    while not done:
        for x in IN:
            if IN[x] == 0:
                n = REQ[x]
                # print(x, n)
                if x == 'ORE':
                    done = True
                    return n
                (nget, need) = F[x]
                amt = (n + nget - 1)//nget
                for (ny, y) in need:
                    if y not in REQ:
                        REQ[y] = 0
                    REQ[y] += amt * ny
                    IN[y] -= 1
                del IN[x]
                break

# print(amount_req)  # part 1

# curr_ore = 1000000000000

low = 0
current = 1e12
    
while low < current:
    mid = (low + current + 1)//2
    if cost(mid) <= int(1e12):
        low = mid
    else:
        current = mid - 1
    
print(low)  # part 2