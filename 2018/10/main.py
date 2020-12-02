fileData = open("10", "r")
lines = fileData.read().split("\n")[:-1]

points = []

for i in lines:
    # can be done in a better way by using regex
    splVel = i.split("velocity=")
    [xVelStr, yVelStr] = splVel[1][1:-1].split(", ")
    (xv, yv)= (int(xVelStr.strip()), int(yVelStr.strip()))
    [xPosStr, yPosStr] = splVel[0].strip().split("position=")[1][1:-1].split(", ")
    (x, y) = (int(xPosStr.strip()), int(yPosStr.strip()))
    points.append((x,y,xv,yv))


def get_next_pos(val):
    (x,y,xv,yv) = val
    return (x+xv,y+yv,xv,yv)

def update(p):
    newp = []
    for i in p:
        newp.append(get_next_pos(i))
    return newp

def display(ps):
    x0 = min(x[0] for x in ps)
    x1 = max(x[0] for x in ps)
    y0 = min(x[1] for x in ps)
    y1 = max(x[1] for x in ps)
    # get diff between them
    dx = x1 - x0
    dy = y1 - y0
    p = set((x[0], x[1]) for x in ps)
    rows = []
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            if (x, y) in p:
                row.append('X')
            else:
                row.append('.')
        rows.append(''.join(row))
    return '\n'.join(rows)

i = 0
while True:
    i += 1
    if abs(i - 10228) < 3:
        d = display(points)
        # part 1
        print(d)
        # part 2
        print(i-1)
    points = update(points)

