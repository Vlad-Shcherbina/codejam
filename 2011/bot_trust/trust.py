import sys
import re
import os
import time
from itertools import *
from pprint import pprint


def solve():
    line = next(fin).split()
    assert int(line.pop(0))*2 == len(line)

    x = [1, 1]
    t = [0, 0]
    total = 0
    for i in range(0, len(line), 2):
        j = 'BO'.index(line[i])
        d = abs(x[j]-int(line[i+1]))
        x[j] = int(line[i+1])
        t[j] = total = max(t[j]+d, total)+1
    
    print>>fout, total


if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out', 'w')

numCases = int(next(fin))
for caseNo in range(numCases):
    print '\b'*10, 100*caseNo/numCases, '%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)