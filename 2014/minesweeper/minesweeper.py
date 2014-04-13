from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj

import random


def solve(fin, fout, only_read):
    r, c, m = map(int, next(fin).split())
    if only_read:
        return
    print(file=fout)

    empty = r * c - m

    random.seed(42)
    for attempt in range(1000):
        solution = {(0, 0)}
        while True:
            if len(solution) == empty:
                if attempt > 20:
                    print(attempt)
                for i in range(r):
                    for j in range(c):
                        if i == j == 0:
                            assert (i, j) in solution
                            fout.write('c')
                        elif (i, j) in solution:
                            fout.write('.')
                        else:
                            fout.write('*')
                    fout.write('\n')
                return

            candidates = list(solution)
            random.shuffle(candidates)
            for i, j in candidates:
                neigh = {(ii, jj)
                    for ii in range(max(0, i - 1), min(i + 2, r))
                    for jj in range(max(0, j - 1), min(j + 2, c))}
                delta = len(neigh - solution)
                if delta > 0 and len(solution) + delta <= empty:
                    break
            else:
                break
            solution |= neigh

    print('Impossible', file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
