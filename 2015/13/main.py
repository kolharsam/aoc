import re
from itertools import permutations

file_lines = open('13.in', 'r')
lines = file_lines.readlines()

inp = []
people = []
for line in lines:
    match = re.findall('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)', line)[0]
    match = list(match)
    match[2] = int(match[2])
    match = tuple(match)
    inp.append(match)
    if match[0] not in people:
        people.append(match[0])

# needed for p2
def add_me():
    for i in people:
        inp.append((i, 'gain', '0', 'Me'))
        inp.append(('Me', 'gain', '0', i))
    people.append('Me')

def get_happiness_scores(p1, p2):
    l = []
    for i in inp:
        if p1 in i and p2 in i:
            l.append(i)
    return l[0], l[1]

def update_score(sc1, sc2, score):
    if 'gain' in sc1:
        score += sc1[2]
    else:
        score -= sc1[2]
    if 'gain' in sc2:
        score += sc2[2]
    else:
        score -= sc2[2]
    return score

def calc_score(current_seating):
    i = 0
    score = 0
    
    while i < len(current_seating)-1:
        l1, l2 = get_happiness_scores(current_seating[i], current_seating[i+1])
        score = update_score(l1, l2, score)
        i += 1
    
    # this is meant for the last and the first seated peeps
    l1, l2 = get_happiness_scores(current_seating[0], current_seating[-1])
    score = update_score(l1, l2, score)
    
    return score

# add_me() - for running part 2
best_score = 0
best_seating = ()
for seating in permutations(people):
    score = calc_score(seating)
    if score > best_score:
        best_score = score
        best_seating = seating

print(best_score, best_seating)
