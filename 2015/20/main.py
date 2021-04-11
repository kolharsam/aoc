num = 34000000

elf_count = {}
def calc_gifts_1(n):
    s = 0
    for i in range(1, num):
        if i > n:
            return s
        if n % i == 0:
            s += 10*i
    return s

def calc_gifts_2(n):
    s = 0
    for i in range(1, num):
        if i > n:
            return s
        if i in elf_count and elf_count[i] >= 50:
            continue
        if n % i == 0:
            s += 10*i
            if i not in elf_count:
                elf_count[i] = 0
            elf_count[i] += 1
    return s

i = 1
while True:
    found = False
    if calc_gifts_1(i) >= num and not found:
        # part 1
        print(i)
        found = True
    if calc_gifts_2(i) >= num:
        # part 2
        print(i)
        break
    i += 1
