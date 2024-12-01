import sys
D = open(sys.argv[1]).read().strip().splitlines()

ranks = {}

def get_rank(s):
    freqs = {}
    for keys in s:
        freqs[keys] = freqs.get(keys, 0) + 1
    
    items_size = freqs.__len__()

    if items_size == 1:
        return 1
    elif items_size == 2:
        vs = freqs.values()
        if 
        

for l in D:
    rank, bid = l.split(' ')
    print(rank, int(bid))

for 
