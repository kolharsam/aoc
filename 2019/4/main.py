start = 234208
end = 765869
cnt = 0
lis = []

while start <= end:
    adj_flg = False
    inc_flg = False
    strt = str(start)
        
    i = 0

    while i < len(strt) - 1:
        if strt[i] == strt[i+1]:
            adj_flg = True 
            break
        i+=1

    stat = strt
    stat = ''.join(sorted(stat))
        
    if stat == strt:
        inc_flg = True
        
    if inc_flg and adj_flg:
        cnt += 1
        lis.append(start)

    start+=1
    
print(len(lis)) # part 1

grps_count = 0
for nu in lis:
    grps = {x : str(nu).count(x) for x in set(str(nu))}
    l = []
    
    for key in grps.keys():
        if grps[key] >= 2 and grps[key] % 2 == 0:
            l.append(key)

    if len(l) > 1:
        grps_count += 1
    
    if len(l) == 1 and grps[l[0]] == 2:
        grps_count+=1

print(grps_count) # part 2
        