lines = [line.strip("\n") for line in open("input")]

PACKETS = {}
last = 0

for i in lines:
    words = i.split(": ")
    packet = int(words[0])
    dep = int(words[1])
    PACKETS[packet] = dep
    if last < packet:
        last = packet # to get the last element

ticker = 0
CAUGHT = []

for i in range(last+1):
    if ticker in PACKETS:
        if ticker % ((PACKETS[ticker] - 1) * 2)  == 0:
            CAUGHT.append((i, PACKETS[ticker]))
    ticker += 1

risk = 0   

for point in CAUGHT:
    a, b = point
    risk += a * b

print(risk) # part 1

caught = False
delay = 0 

# brute force may not be the best approach for this 
# but nevertheless, it does take its own sweet time to get to the solution

while not caught:
    CAUGHT = []
    ticker = 0
    for i in range(last+1):
        if i in PACKETS:
            print(ticker + delay, ticker)
            if (ticker + delay) % ((PACKETS[ticker] - 1) * 2)  == 0:
                CAUGHT.append((i, PACKETS[ticker]))
        ticker += 1
    
    if len(CAUGHT) == 0:
        caught = True
        print(delay) # part 2
    else:
        delay += 1

