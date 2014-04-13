from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj


def fair_score(naomis, kens):
    result = 0
    q = len(kens)
    for x in reversed(naomis):
        if x > kens[q - 1]:
            result += 1
        else:
            q -= 1

    return result


def cheating_score(naomis, kens, k):
    result = 0
    for i in range(len(naomis) - k):
        if naomis[i + k] > kens[i]:
            result += 1
    return result


def solve(fin, fout, only_read):
    n = int(next(fin))
    naomis = sorted(map(float, next(fin).split()))
    kens = sorted(map(float, next(fin).split()))
    assert n == len(naomis) == len(kens)
    if only_read:
        return

    best_score = max(cheating_score(naomis, kens, k) for k in range(0, n))

    print(best_score, fair_score(naomis, kens), file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
