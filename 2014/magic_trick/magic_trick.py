from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj


def solve(fin, fout, only_read):
    sol = set(range(1, 17))

    for _ in range(2):
      r = int(next(fin))
      for i in range(4):
        row = next(fin)
        if i + 1 == r:
          sol &= set(map(int, row.split()))

    if only_read:
        return

    if len(sol) == 0:
      print('Volunteer cheated!', file=fout)
    elif len(sol) > 1:
      print('Bad magician!', file=fout)
    else:
      sol, = sol
      print(sol, file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
