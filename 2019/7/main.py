from itertools import permutations

IN = [int(x) for x in open('input').read().split(',')]
P = [x for x in IN]

phase = [9,8,7,6,5] 
PERMS = []

for perm in permutations(phase, len(phase)):
    PERMS.append(list(perm))

def run(inputs, ip):
    while True:
        digits = [int(x) for x in str(P[ip])]
        opcode = (0 if len(digits) == 1 else digits[-2])*10 +digits[-1]
        digits = digits[:-2]

        if opcode == 1:
            while len(digits) < 3:
                digits = [0] + digits
            op1, op2, op3 = P[ip+1], P[ip+2], P[ip+3]
            P[op3] = (op1 if digits[2]==1 else P[op1])+(op2 if digits[1] == 1 else P[op2])
            ip+=4
        elif opcode == 2:
            while len(digits) < 3:
                digits = [0] + digits
            op1, op2, op3 = P[ip+1], P[ip+2], P[ip+3]
            P[op3] = (op1 if digits[2]==1 else P[op1])*(op2 if digits[1] == 1 else P[op2])
            ip+=4
        elif opcode == 3:
            op1 = P[ip+1]
            P[op1] = inputs[0] 
            inputs.pop(0)
            ip+=2
        elif opcode == 4:
            op1 = P[ip+1]
            ip += 2
            return P[op1], ip
        elif opcode == 5:
            while len(digits) < 2:
                digits = [0]+digits
            op1,op2 = P[ip+1], P[ip+2]
            if (op1 if digits[1] == 1 else P[op1]) != 0:
                ip = (op2 if digits[0]==1 else P[op2])
            else:
                ip+=3
        elif opcode == 6:
            while len(digits) < 2:
                digits = [0]+digits
            op1,op2 = P[ip+1], P[ip+2]
            if (op1 if digits[1] == 1 else P[op1]) == 0:
                ip = (op2 if digits[0]==1 else P[op2])
            else:
                ip+=3
        elif opcode == 7:
            while len(digits) < 3:
                digits = [0]+digits
            op1,op2,op3 = P[ip+1], P[ip+2], P[ip+3]    
            if (op1 if digits[2] == 1 else P[op1]) < (op2 if digits[1] == 1 else P[op2]):
                P[op3] = 1
            else:
                P[op3] = 0
            ip += 4
        elif opcode == 8:
            while len(digits) < 3:
                digits = [0]+digits
            op1,op2,op3 = P[ip+1], P[ip+2], P[ip+3]
            if (op1 if digits[2] == 1 else P[op1]) == (op2 if digits[1] == 1 else P[op2]):
                P[op3] = 1
            else:
                P[op3] = 0
            ip += 4
        else:
            assert opcode == 99, opcode
            return None, ip

ans = 0

for perm in PERMS:
    val=0
    d_ip = [0 for _ in range(len(perm))]
    d_val = [0 for _ in range(len(perm))]
    print(d_ip, d_val)
    RUNQ = [[perm[i]] for i in range(len(perm))]
    RUNQ[0].append(0)
    fin = False

    while not fin:
        for i in range(len(perm)):
            val, ret_ip = run(RUNQ[i], d_ip[i])
            if val == None:
                print(perm, d_val[-1])
                if d_val[-1] > ans:
                    ans = d_val[-1]
                fin = True
                break
            d_ip[i] = ret_ip
            if val != None:
                d_val[i] = val
            RUNQ[(i+1)%len(RUNQ)].append(val)

print(ans) # part 1