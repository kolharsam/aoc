input = [line.strip("\n") for line in open("input")]

grid = []
count = 1

i, j = 0, 0

while i < 3:
    new = []
    while j < 3:
        new.append(count)
        j+=1
        count+=1
    i+=1
    grid.append(new)
    j = 0

x, y = 1, 1

DIRECTIONS = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

ans = []

for i in input:
    word = i
    for letter in word:
        delx, dely = DIRECTIONS[letter]
        x = (x+delx if x+delx >= 0 and x+delx < 3 else x)
        y = (y+dely if y+dely >= 0 and y+dely < 3 else y)
    ans.append(grid[x][y])

print(''.join(list(map(str, ans)))) # part 1

# this is the simplest way to represent the grid, if you're looking at this and have solved it 
# with a better and cleaner approach. I'm all ears

grid = [['0','0','1','0','0'], ['0','2','3','4','0'], ['5','6','7','8','9'], ['0','A','B','C','0'], ['0','0','D','0','0']]

x, y = 2,0
deadend = '0'
ans = []

for i in input:
    word = i
    for letter in word:
        delx, dely = DIRECTIONS[letter]
        tempx, tempy = x+delx, y+dely
        if tempx >= 0  and tempx < 5 and tempy >= 0 and tempy < 5:
            if grid[tempx][tempy] != deadend:
                x = tempx
                y = tempy
    ans.append(grid[x][y])

print(''.join(ans)) # part 2
        