import sys

infile = sys.argv[1] if len(sys.argv)>1 else '6.in'
sub = int(sys.argv[2]) if len(sys.argv)>2 else 14 # sub = 4 for part 1
data = open(infile).read().strip().split('\n')[0]

le = len(data)

for i in range(le-sub):
    seq = data[i:i+sub]
    sett = set(seq)
    if sett.__len__() == seq.__len__():
        print(i+sub)
        break
