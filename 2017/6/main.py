with open('input') as reader:
    input = reader.read()

allStates = []

def processInput():
    temp = input.split("\t")
    temp = list(map(int, temp))
    return temp

def getMax(num_list):
    temp = sorted(num_list)
    size = len(temp)
    maxElem = temp[size-1]
    position = num_list.index(maxElem)
    return maxElem, position

def isPresent(current):
    flag = True
    
    try:
        allStates.index(current)
    except ValueError:
        flag = False
    
    return flag

def redistribute(state, largest, position):
    n = 0
    pointer = position + 1
    state[position] = 0
    size = len(state)

    while n < largest:
        state[pointer % size] += 1
        pointer += 1
        n += 1

    return state

def fun(inputs, count):
    while True:
        if isPresent(inputs):
            print(count)
            print(count - allStates.index(inputs))
            break
        else:
            input_copy = inputs.copy()
            large, pos = getMax(input_copy)
            count+=1
            red = redistribute(input_copy, large, pos)
            allStates.append(inputs)
            inputs = red

if __name__ == "__main__":
    int_input = processInput()
    # int_input = [0,2,7,0]
    fun(int_input, 0)
    