IN = [int(x) for x in open('input').read().split(',')]

P = [x for x in IN]

ip = 0

while True:
    digits = [int(x) for x in str(P[ip])]
    opcode = (0 if len(digits) == 1 else digits[-2])*10 +digits[-1]
    digits = digits[:-2]

    print(digits)

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
        P[op1] = 5 # will be used only once
        ip+=2
    elif opcode == 4:
        op1 = P[ip+1]
        print(P[op1])
        ip+=2
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
    elif opcode == 99:
        break