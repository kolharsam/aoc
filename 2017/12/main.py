import collections

input = [line.strip("\n") for line in open("input")]

graph = collections.defaultdict(list)

for i in input:
    nodes = i.strip().split()

    par = int(nodes[0])
    childs = map(lambda x: int(x.strip(',')), nodes[2:])

    for child in childs:
        graph[par].append(child)
        graph[child].append(par)

CONNECTED = set()
groups = 0

for i in range(2000):
    if i in CONNECTED:
        continue
    groups += 1
    Q = [i]
    while Q:
        node = Q.pop()
        for ch in graph[node]:
            if ch not in CONNECTED:
                CONNECTED.add(ch)
                Q.append(ch)

print(groups)


