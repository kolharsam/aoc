import sys
D = open(sys.argv[1]).read().strip().splitlines()

seeds = []

seed2soil = []
soil2fert = []
fert2watr = []
watr2lite = []
lite2temp = []
temp2humd = []
humd2locn = []

i = 0

while i < len(D):
    l = D[i]
    if l.startswith('seeds: '):
        ssp = l.split(" ")
        seeds = list(map(int,ssp[1:]))

    if l.startswith('seed-to-soil'):
        i+=1
        while D[i] != '':
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            seed2soil.append(ll)
            i+=1

    if l.startswith('soil-to-fertilizer'):
        i+=1
        while D[i] != '':
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            soil2fert.append(ll)
            i+=1

    if l.startswith('fertilizer-to-water'):
        i+=1
        while D[i] != '':
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            fert2watr.append(ll)
            i+=1
    
    if l.startswith('water-to-light'):
        i+=1
        while D[i] != '':
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            watr2lite.append(ll)
            i+=1

    if l.startswith('light-to-temperature'):
        i+=1
        while D[i] != '':
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            lite2temp.append(ll)
            i+=1

    if l.startswith('temperature-to-humidity'):
        i+=1
        while D[i] != '':
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            temp2humd.append(ll)
            i+=1
    
    if l.startswith('humidity-to-location'):
        i+=1
        while i < len(D):
            l = D[i]
            ll = tuple(map(int, l.split(' ')))
            humd2locn.append(ll)
            i+=1

    i+=1

# print(seeds)
# print(seed2soil)
# print(soil2fert)
# print(fert2watr)
# print(watr2lite)
# print(lite2temp)
# print(temp2humd)
# print(humd2locn)

low_loc = -1

def get_location(slc):
    return False

for s in seeds:
    s_loc = get_location(s)
    low_loc = min(s_loc, low_loc)

print(low_loc) # p1
