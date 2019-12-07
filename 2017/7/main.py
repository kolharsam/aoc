from collections import defaultdict

def dfs(children, weights, root):
    exp = None
    s = weights[root]
    for child in children[root]:
        w = dfs(children, weights, child)
        s += w
        if exp is None:
            exp = w
        elif exp != w:
            print('expected child: ', child, 'to have w :', exp, 'has : ', w)
            print(w - weights[child])
    return s

nodes = []
tree = set()
weights = {}
children = defaultdict(list)

for line in open("input"):
    line = line.strip().split()
    nodes.append(line[0])
    weights[line[0]] = int(line[1].strip('()'))

    if '->' in line:
        i = line.index('->')
        children[nodes[-1]] = [c.strip(',') for c in line[i + 1:]]
        tree |= set(children[nodes[-1]])

for node in nodes:
    if node not in tree:
        root = node

dfs(children, weights, root)