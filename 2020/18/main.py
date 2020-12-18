import ast

file_inp = open("18.in", "r")
lines = file_inp.read().splitlines()
exprs = []
for line in lines:
    line = [x for x in line if x != ' ']
    exprs.append(line)

def evaluate(expr):
    storage = []
    it = 0
    n = 0
    lastOp = ''
    while it != len(expr):
        current = expr[it]
        if current == '*' or current == '+':
            lastOp = current
        elif current != '(' and current != ')':
            storage.append(int(current))
            if len(storage) == 2:
                if lastOp == '+':
                    n = sum(storage)
                    storage = [n]
                elif lastOp == '*':
                    k = 1
                    for g in storage:
                        k *= g
                    n = k
                    storage = [n]
        elif current == '(':
            it2 = it+1
            opens = 1
            acc = []
            while opens != 0:
                if expr[it2] == ')':
                    opens-=1
                elif expr[it2] == '(':
                    opens+=1
                acc.append(expr[it2])
                it2+=1
            storage.append(evaluate(acc[:-1]))
            it += len(acc)
            if len(storage) == 2:
                if lastOp == '+':
                    n = sum(storage)
                    storage = [n]
                elif lastOp == '*':
                    k = 1
                    for g in storage:
                        k *= g
                    n = k
                    storage = [n]
            continue
        it += 1
    return n

sums = []
for expr in exprs:
    sums.append(evaluate(expr))

# part 1
print(sum(sums))


# Use ast to parse tokens. Manipulate operators to force evaluation order.
# A less hacky solution would be to just use a proper token parser like
# https://www.geeksforgeeks.org/expression-evaluation/ and set precedence
# of operators accordingly.
def value(expr):
    return expr.value if type(expr) is ast.Constant else eval_binop(expr)


def eval_binop(b):
    left = value(b.left)
    right = value(b.right)
    op = op = int.__add__ if type(b.op) is ast.Div else int.__mul__
    return op(left, right)

# Part two
# Replace * with + to increase priority.
print(sum(eval_binop(
    ast.parse(l.replace('+', '/').replace('*', '+')).body[0].value) for l in lines
))