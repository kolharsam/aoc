with open("input") as reader:
    input = reader.read()

level = 0
pos = 0

for i in input:
    if i == '(':
        level+=1
    elif i == ')':
        level-=1

print(level) # part 1

level = 0

for i in input:
    if i == '(':
        level+=1
        pos+=1
    elif i == ')':
        level-=1
        pos+=1
    if level == -1:
        print(pos) # part 2
        break


