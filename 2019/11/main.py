class IntcodeComputer(object):

    def __init__(self, pid, program_file, input):
        self.instructions = [int(x) for x in open(program_file).read().split(",")]
        self.input = input
        self.ip = 0
        self.pid = pid
        self.relative_base = 0

    def index(self, i, I):
        mode = (0 if i >= len(I) else I[i])
        val = self.instructions[self.ip+1+i]
        if mode == 0:
            pass
        elif mode == 1:
            assert False
        elif mode == 2:
            val += self.relative_base
        while len(self.instructions) <= val:
            self.instructions.append(0)
        return val
    def val(self, i, I):
        mode = (0 if i>=len(I) else I[i])
        val = self.instructions[self.ip+1+i]
        if mode == 0:
            while len(self.instructions) <= val:
                self.instructions.append(0) 
            val = self.instructions[val]
        elif mode == 2:
            val = self.instructions[val + self.relative_base]
        return val

    def run(self):
        while True:
            cmd = str(self.instructions[self.ip])
            opcode = int(cmd[-2:])
            I = list(reversed([int(x) for x in cmd[:-2]]))
            if opcode == 1:
                self.instructions[self.index(2, I)] = self.val(0, I) + self.val(1, I)
                self.ip += 4
            elif opcode == 2:
                self.instructions[self.index(2, I)] = self.val(0, I) * self.val(1, I)
                self.ip += 4
            elif opcode == 3:
                inp = self.input()
                self.instructions[self.index(0, I)] = inp
                # self.inserts.pop()
                self.ip += 2
            elif opcode == 4:
                ans = self.val(0, I)
                self.ip += 2
                return ans
            elif opcode == 5:
                self.ip = self.val(1, I) if self.val(0, I) != 0 else self.ip+3
            elif opcode == 6:
                self.ip = self.val(1, I) if self.val(0, I) == 0 else self.ip+3
            elif opcode == 7:
                self.instructions[self.index(2, I)] = (1 if self.val(0, I) < self.val(1, I) else 0)
                self.ip += 4
            elif opcode == 8:
                self.instructions[self.index(2, I)] = (1 if self.val(0, I) == self.val(1, I) else 0)
                self.ip += 4
            elif opcode == 9:
                self.relative_base += self.val(0, I)
                self.ip += 2
            else:
                assert opcode == 99, opcode
                return None


R = 100
C = 100

GR = [[0 for _ in range(C)] for _ in range(R)]
r,c = R//2, C//2
GR[r][c] = 1
d = 0

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def get_Colour():
    return GR[r][c]

painted = set()
P = IntcodeComputer('0', 'input', get_Colour)

while True:
    color = P.run()
    # print(color)
    if color == None:
        break
    GR[r][c] = color
    painted.add((r, c))
    turn = P.run()
    if turn == 0:
        d = (d+1)%4
    else:
        d = (d+3)%4
    # print(d)
    r += DR[d]
    c += DC[d]

# print(len(painted)) # part 1

for r in range(R):
    for c in range(C):
        print('0' if GR[r][C-c-1]==1 else ' ', end='') # part 2
    print()