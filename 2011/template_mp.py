from __future__ import division
import sys
import re
import os
import time
from itertools import *
from pprint import pprint
from copy import copy
import multiprocessing
from cStringIO import StringIO

mp = False

###################################


def solve(fin, fout, only_read=False):
    n = int(next(fin))

    if only_read:
        return

    print>>fout, 'ok'


###################################

class ListIterator(object):
    def __init__(self, list):
        self.list = list
        self.i = 0

    def next(self):
        if self.i >= len(self.list):
            raise StopIteration()
        self.i += 1
        return self.list[self.i-1]


def task(fin):
   fout = StringIO()
   solve(fin, fout)
   sys.stderr.write('.')
   return fout.getvalue()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'specify input file'
        exit()

    startTime = time.clock()

    fin = open(sys.argv[1])
    lines = fin.readlines()
    fin.close()

    fin = ListIterator(lines)

    numCases = int(next(fin))

    fins = []

    for caseNo in range(numCases):
        fins.append(copy(fin))
        solve(fin, None, only_read=True)
    try:
        next(fin)
        assert False, 'not all lines are processed'
    except StopIteration:
        pass

    print>>sys.stderr, '['+' '*len(fins)+']'
    sys.stderr.write('[')

    if mp:
        pool = multiprocessing.Pool()
        results = pool.map(task, fins)
    else:
        results = map(task, fins)

    sys.stderr.write(']\n')

    fout = open(os.path.splitext(sys.argv[1])[0]+'.out', 'w')
    for caseNo, answer in enumerate(results):
        print>>fout, 'Case #%s:'%(caseNo+1), answer,
    fout.close()

    print '\b'*10+'it took %.1fs'%(time.clock()-startTime)