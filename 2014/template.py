from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj


def solve(fin, fout, only_read):
    n = int(next(fin))
    if only_read:
        return
    print('zzz', file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
