with open('input') as reader:
    input = reader.read()

allIntInput = []

def processInput():
    allInput = input.split(",")
    return list(map(int, allInput))

if __name__ == "__main__":
    allIntInput = processInput()
    
    pos = 0

    noun = 0
    verb = 0
    # allIntInput[1] = 38
    # allIntInput[2] = 92

    while True:
        if allIntInput[pos] == 1:
            add1 = allIntInput[pos+1]
            add2 = allIntInput[pos+2]
            sums = allIntInput[add1] + allIntInput[add2]
            allIntInput[allIntInput[pos+3]] = sums
            pos += 4
        elif allIntInput[pos] == 2:
            prod = allIntInput[allIntInput[pos+1]] * allIntInput[allIntInput[pos+2]]
            allIntInput[allIntInput[pos+3]] = prod
            pos += 4
        elif allIntInput[pos] == 99:
            break
        
    
    print(allIntInput[0], (100 * 38 + 92), len(allIntInput))    
        