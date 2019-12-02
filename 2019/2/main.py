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
    # instead of using brute force to solve this, since the noun and the verb lie as integers btw 0 and 99
    # increase noun from 12 to 99 along with the verb being iterated across 2 to 99
    # since the answer we have to reach -> 19690720 is greater than for 12 2 's answer.

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
        