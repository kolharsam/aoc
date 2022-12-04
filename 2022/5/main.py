import sys

infile = sys.argv[1] if len(sys.argv)>1 else '5.in'
data = open(infile).read().strip().split('\n')
