from itertools import product

def count_ques(s):
    count = 0
    for l in s:
        if l == '?':
            count += 1
    return count

def cj_jc_counter(st):
    cj = 0
    jc = 0
    for idx, l in enumerate(st[:-1]):
        if l == 'C' and st[idx+1] == 'J':
            cj += 1
        elif l == 'J' and st[idx+1] == 'C':
            jc += 1 
    return (cj, jc)

def place_into_string(pat, choices, num):
    i = 0
    nstr = ""
    for l in pat:
        if l == '?':
            nstr += choices[i]
            i += 1
        else:
            nstr += l
    return nstr

def get_all_patterns(pattern, num_ques):
    tot = 2 * num_ques
    l = []
    
    for p in product(['C', 'J'], repeat=tot):
        l.append(place_into_string(pattern, p, num_ques))
    
    return l

def calc_min_cost(pattern, num_ques, cost_x, cost_y):
    pats = get_all_patterns(pattern, num_ques)
    costs = []

    for pat in pats:
        cj_count, jc_count = cj_jc_counter(pat)
        costs.append(cj_count*cost_x + jc_count*cost_y)

    return min(costs)

times = int(input())
case = 1

while times > 0:
    cin = input().split()
    x = int(cin[0])
    y = int(cin[1])
    pat = cin[-1]
    c = count_ques(pat)
    min_cost = calc_min_cost(pat, c, x, y)
    print(f"Case #{case}: {min_cost}")
    times -= 1
    case += 1
