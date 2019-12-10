import math

input = [line.strip('\n') for line in open('input')]

number_of_asteroids = 0
asteroids = []
x = 0
y = 0
max_x = len(input[0])

for line in input:
    for obj in line:
        if obj == '#':
            asteroids.append((x, y))
        x += 1
    y += 1
    x = 0

number_of_asteroids = len(asteroids)
max_sights = 0
LINE_SIGHTS = []
max_pointx , max_pointy = 0,0

for ast in asteroids:
    ast_x, ast_y = ast
    sights = set()
    for s in asteroids:
        if ast != s:
            cur_x, cur_y = s
            dy = ast_y - cur_y
            dx = ast_x - cur_x
            g = math.gcd(dy, dx)  # this is done to normalize - so that the slope that are dissimilar are easily detected
            if g < 0:
                g *= -1
            slope = (((-dy//g),(dx//g)))
            sights.add(slope)
    if len(sights) > max_sights:
        max_sights = len(sights)
        LINE_SIGHTS.clear()
        max_pointx = ast_x
        max_pointy = ast_y
        for l in sights:
            LINE_SIGHTS.append(l)
        
print(max_sights) # part 1

sorted_slopes = []
for (dy, dx) in LINE_SIGHTS:
    s = math.atan2(dy, dx)
    if s > math.pi*2:
        s -= 2*math.pi/2.0
    sorted_slopes.append((s, (dy, dx)))

sorted_slopes = list(reversed(sorted(sorted_slopes)))
bet_x, bet_y = sorted_slopes[199][1]

a = abs(max_pointx+bet_x)
b = abs(max_pointy-bet_y)

print(a*100 + b) # part 2
