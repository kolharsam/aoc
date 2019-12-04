import numpy as np

with open("input") as reader:
    input = reader.read()

inputasread = input
input = list(map(int, input.split(",")))

# rules : 
# list begins at index 0
# take the first n elements from the loop and group them within ()
# reverse all elements in ( )
# current pointer moves forward by n + skip size
# inc skip size and repeat

ln = 256

def getRing():
    temp = []
    for i in range(ln):
        temp.append(i)
    return temp

def playwithring(ring):
    skip = 0
    start = 0

    for i in input:
        newr = ring.copy()
        for num in range(i):
            newr[(start + num) % ln] = ring[(start + i - num - 1) % ln]
        ring = newr
        start += (i + skip) % ln
        skip+=1

    print(ring[0] * ring[1]) 

def playwithring2(ins):
    in2 = ins + [17, 31, 73, 47, 23]
    ri = getRing()
    ln = 256
    skip = 0
    start = 0

    for _ in range(64):
        for l in in2:
            newr = ri.copy()
            for t in range(l):
                newr[(start+t) % ln] = ri[(start + l - t - 1) % ln]
            ri = newr
            start += l + skip
            skip+= 1
    
    sparse_hash = ri
    dense_hash = np.array(sparse_hash)

    print(''.join(hex(x)[2:].zfill(2) for x in np.bitwise_xor.reduce(dense_hash.reshape(16, 16), axis=1)))

if __name__ == "__main__":
    ring = getRing()
    playwithring(ring)
    playwithring2([ord(c) for c in inputasread])
