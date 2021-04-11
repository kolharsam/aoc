from copy import copy

lines = open('input', 'r').read().split("\n\n")

reps = [x.split(" => ") for x in lines[0].split("\n")]
inp = lines[1].strip()
res = set()

def make_new_word(idx, start_seq, replacement, inp_copy):
    start_seq_len = len(start_seq)

    if start_seq_len == 1:
        if inp_copy[idx] == start_seq:
            return inp_copy[:idx] + replacement + inp_copy[idx+1:]
        else:
            return None
    
    if idx+start_seq_len >= len(inp_copy) or inp_copy[idx:(idx+start_seq_len)] != start_seq:
        return None

    return inp_copy[:idx] + replacement + inp_copy[(idx+start_seq_len):]

for idx, _ in enumerate(inp):
    for comb in reps:
        new_word = make_new_word(idx, comb[0], comb[1], copy(inp))
        if new_word != None:
            res.add(new_word)
 
# part 1
print(len(res))

def calc_steps(w, c):
    if len(w) > len(inp):
        return c
    
    for idx, _ in enumerate(w):
        found = False
        for comb in reps:
            new_word = make_new_word(idx, comb[0], comb[1], copy(w))
            # print(new_word, c)
            if new_word != None:
                if new_word == inp:
                    found = True
                    break
                else:
                    # print(c, len(w), len(inp))
                    calc_steps(new_word, c+1)
        if found == True:
            print(c+1, "FOUND!!")
            break
    
    return c

# part 2
calc_steps("e", 0)
