from __future__ import division
import sys
import re
import os
import time
from itertools import *
from pprint import pprint


def solve():
    print>>fout, "ok"


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

try:
    next(fin)
    assert False, 'not all lines are processed'
except StopIteration:
    pass

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)