from __future__ import print_function
import sys
import re
import os
import argparse
from timeit import default_timer
from pprint import pprint
from copy import copy
import multiprocessing
import zipfile

if sys.version_info[0] == 3:
    from io import StringIO
else:
    from StringIO import StringIO


def main(solve, *source_files):
    global _solve
    # For calling from parallel map (fork-based implementations only).
    _solve = solve

    assert source_files

    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help="input file")
    parser.add_argument('--mp', action='store_true', help="use multiprocessing")
    args = parser.parse_args()
    print(args)

    with zipfile.ZipFile('solution.zip', 'w') as zout:
        for source_file in list(source_files) + [__file__]:
            zout.write(source_file, os.path.basename(source_file))

    start_time = default_timer()

    with open(args.input) as fin:
        lines = fin.readlines()

    fin = ListIterator(lines)

    num_cases = int(next(fin))

    fins = []

    for _ in range(num_cases):
        fins.append(copy(fin))
        solve(fin, None, only_read=True)
    try:
        next(fin)
        assert False, 'not all lines are processed'
    except StopIteration:
        pass

    sys.stderr.write('[' + ' '*len(fins) + ']\n')
    sys.stderr.write('[')

    if args.mp:
        pool = multiprocessing.Pool()
        results = pool.map(task, fins)
    else:
        results = map(task, fins)

    with open(os.path.splitext(args.input)[0]+'.out', 'w') as fout:
        for case_no, answer in enumerate(results):
            print('Case #{}:'.format(case_no + 1), answer, file=fout, end='')

    sys.stderr.write(']\n')

    print('it took {:.3}s'.format(default_timer() - start_time))


def task(fin):
    fout = StringIO()
    _solve(fin, fout, only_read=False)
    sys.stderr.write('.')
    sys.stderr.flush()
    return fout.getvalue()


class ListIterator(object):
    def __init__(self, list):
        self.list = list
        self.i = 0

    def next(self):
        if self.i >= len(self.list):
            raise StopIteration()
        self.i += 1
        return self.list[self.i-1]

    # for python 3.*
    __next__ = next
