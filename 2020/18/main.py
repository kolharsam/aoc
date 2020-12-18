file_inp = open("18-sample.in", "r")
lines = file_inp.read().splitlines()

exprs = []

for line in lines:
    line = [x for x in line if x != ' ']
    exprs.append(line)

sums = []

def evaluate(expr):
    storage = []
    it = 0
    n = 0
    lastOp = ''
    while it != len(expr):
        current = expr[it]
        print(current, it)
        if current == '*' or current == '+':
            lastOp = current
        elif current != '(' and current != ')':
            storage.append(int(current))
            if len(storage) == 2:
                if lastOp == '+':
                    n += sum(storage)
                    storage = [n]
                elif lastOp == '*':
                    k = 1
                    for g in storage:
                        k *= g

                    n += k
                    storage = [n]

uzzzz           it2 = it+1
            opens = 1
            acc = []
            while opens != 0:
                if expr[it2] == ')':
                    opens-=1
                elif expr[it2] == '(':
                    opens+=1

                acc.append(expr[it2])
                it2+=1

            print(acc[:-1])
            storage.append(evaluate(acc[:-1]))
            it += len(acc)
            continue

        it += 1
        print(storage)
    return n

for expr in exprs:
    if "//" in expr:
        continue

    sums.append(evaluate(expr))

print(sums)
# part1
print(sum(sums))
