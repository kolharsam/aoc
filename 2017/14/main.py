import numpy as np

ln = 256

def getRing():
    temp = []
    for i in range(ln):
        temp.append(i)
    return temp

def knothash(ins):
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

    # pylint: disable=no-member
    return(''.join(hex(x)[2:].zfill(2) for x in np.bitwise_xor.reduce(dense_hash.reshape(16, 16), axis=1)))

if __name__ == "__main__":
    starter = "jxqlasbh"
    num = 0
    BINARIES = []
    while num < 128:
        inp = starter + "-" + str(num)
        res = knothash([ord(c) for c in inp])
        binary = "{0:08b}".format(int(res, 16))   # most important function
        if len(binary) <= 128:
            BINARIES.append(binary)
        else:
            while len(binary) <= 128:
                binary = '0' + binary 
        num += 1
    
    onec = 0

    for row in BINARIES:
        for char in row:
            if char == '1':
                onec += 1

    print(onec) # part 1
