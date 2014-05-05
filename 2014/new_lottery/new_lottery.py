from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj

import collections


def solve(fin, fout, only_read):
    a, b, k = map(int, next(fin).split())
    if only_read:
            return

    def hz(n, i, threshold_bit):
        if i < threshold_bit:
            return [0, 1]
        if i == threshold_bit:
            return [0]
        return [(n >> i) & 1]

    result = 0
    for qa in range(31):
        if a & (1 << qa) == 0:
            continue
        for qb in range(31):
            if b & (1 << qb) == 0:
                continue
            for qc in range(31):
                if (k + 1) & (1 << qc) == 0:
                    continue

                mm = 1
                for i in range(31):
                    m = 0
                    for bit_a in hz(a, i, qa):
                        for bit_b in hz(b, i, qb):
                            if bit_a & bit_b in hz(k + 1, i, qc):
                                m += 1
                    mm *= m
                result += mm

    print(result, file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
