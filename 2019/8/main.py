with open("input") as reader:
    input = reader.read()

WIDTH = 25
HEIGHT = 6
pixel = 0
LAYERS = []
ZEROS = []
MESSAGE = []

while pixel < len(input):
    layer = []
    for i in range(HEIGHT * WIDTH):
        layer.append(input[pixel])
        pixel += 1
    LAYERS.append(layer)

for layer in LAYERS:
    zeros = 0
    ones = 0
    twos = 0
    for pix in layer:
        if pix == '0':
            zeros += 1
        if pix == '1':
            ones += 1
        if pix == '2':
            twos += 1
    ZEROS.append((zeros, ones, twos))

ZEROS.sort()
zres, ores, tres = ZEROS[0]
print(ores * tres)  # part 1

message = []

for i in range(WIDTH * HEIGHT):
    pixels = []
    
    for pix in range(len(LAYERS)):
        pixels.append(LAYERS[pix][i])

    for p in pixels:
        if p == '0':
            message.append('.')
            break
        elif p == '1':
            message.append('1')
            break

p = 0
for i in range(HEIGHT):
    mes = ""
    for j in range(WIDTH):
        mes += message[p]
        p += 1
    MESSAGE.append(mes)

for i in MESSAGE:
    print(i) # part 2 