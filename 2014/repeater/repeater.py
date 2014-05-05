from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj


def counts(s):
    cnt = 0
    prev = '-'
    result = []
    for c in s:
        if c == prev:
            cnt += 1
        else:
            if cnt:
                result.append((prev, cnt))
            cnt = 1
            prev = c
    if cnt:
        result.append((prev, cnt))
    return result


assert counts('aa') == [('a', 2)]
assert counts('abba') == [('a', 1), ('b', 2), ('a', 1)]


def solve(fin, fout, only_read):
    n = int(next(fin))
    strings = []
    for _ in range(n):
        strings.append(next(fin))

    if only_read:
        return

    pairs = list(map(counts, strings))
    if len(set(map(len, pairs))) != 1:
        print('Fegla Won', file=fout)
        return

    result = 0
    for i in range(len(pairs[0])):
        chars = set(p[i][0] for p in pairs)
        ns = [p[i][1] for p in pairs]
        if len(set(chars)) != 1:
            print('Fegla Won', file=fout)
            return
        ns.sort()
        for q in ns:
            result += abs(q - ns[len(ns) // 2])
    print(result, file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
