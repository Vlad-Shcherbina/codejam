from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj


def solve(fin, fout, only_read):
    c, f, x = map(float, next(fin).split())
    if only_read:
        return

    t = 0.0
    r = 2

    while c * (r + f) < x * f:
        t += c / r
        r += f

    t += x / r

    print(t, file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
