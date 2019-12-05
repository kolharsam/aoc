import itertools

input = [line.rstrip('\n') for line in open("input")]

res2 = 0
res3 = 0

for word in input:
    count = {i: word.count(i) for i in set(word)}
    counted2 = False
    counted3 = False
    for key in count:
        if count[key] == 2 and counted2 == False:
            counted2 = True
            res2 += 1
        if count[key] == 3 and counted3 == False:
            counted3 = True
            res3 += 1

print(res2 * res3) # part 1

for w1, w2 in itertools.combinations(input, 2):
    if sum(l1 == l2 for l1, l2 in zip(w1, w2)) == len(w1) - 1:
        print(''.join(l1 for l1, l2 in zip(w1, w2) if l1 == l2))