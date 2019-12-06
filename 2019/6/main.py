from collections import deque

EDGES = {}

for line in open("input").readlines():
    a,b = line.strip().split(")")
    if a not in EDGES:
        EDGES[a] = []
    if b not in EDGES:
        EDGES[b] = []
    EDGES[a].append(b)
    EDGES[b].append(a)

DISTANCES = {}

VISITED = deque()
VISITED.append(('YOU', 0))

# this is a standard BFS algo, you are going through every node possible from a start node
# and you will move into every node possible from that start node and calculating the distance accordingly

while VISITED:
    planet, distance = VISITED.popleft()
    if planet in DISTANCES:
        continue
    DISTANCES[planet] = distance
    for edge in EDGES[planet]:
        VISITED.append((edge, distance+1))

print(DISTANCES['SAN'] - 2)
# doing distance - 2 as the answer does not require the start YOU and end SAN