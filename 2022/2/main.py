import sys

infile = sys.argv[1] if len(sys.argv)>1 else '2.in'
data = open(infile).read().strip().split('\n')

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

score = 0
score2 = 0

you = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}
me = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

def findWinner(them: str, mine: str, pt2: bool):
    ct = you[them]
    mt = me[mine]
    global score2
    
    if pt2:
        if mine == 'X':
            if ct == 'rock':
                score2 += scores['Z']
            elif ct == 'paper':
                score2 += scores['X']
            elif ct == 'scissors':
                score2 += scores['Y']
            return -1
        elif mine == 'Y':
            score2 += scores[them]
            return 0
        elif mine == 'Z':
            if ct == 'rock':
                score2 += scores['Y']
            elif ct == 'paper':
                score2 += scores['Z']
            elif ct == 'scissors':
                score2 += scores['X']
            return 1    
    
    if ct == mt:
        return 0
    if (ct == 'rock' and mt == 'paper') or (ct == 'paper' and mt == 'scissors') or (ct == 'scissors' and mt == 'rock'):
        return 1
    
    return -1

for line in data:
    [y, m] = line.split()
    score += scores[m]
    sc = findWinner(y, m, False)
    sc2 = findWinner(y, m, True)
    if sc == 0:
        score += 3
    elif sc == 1:
        score += 6
    if sc2 == 0:
        score2 += 3
    elif sc2 == 1:
        score2 += 6

# part 1
print(score)
# part 2
print(score2)
