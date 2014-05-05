from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj

import sys
import collections
import itertools


def solve(fin, fout, only_read):
    n = int(next(fin))
    result = 10

    adj = collections.defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, next(fin).split())
        adj[a].append(b)
        adj[b].append(a)

    if only_read:
        return

    sts = set()
    subtrees_order = []
    def rec(fr, v):
        for v2 in adj[v]:
            if v2 != fr:
                rec(v, v2)
        if (v, fr) not in sts:
            sts.add((v, fr))
            subtrees_order.append((v, fr))

    for a, bs in adj.items():
        for b in bs:
            rec(a, b)

    sizes = {}
    bin_costs = {}

    def hz(v, children):
        if len(children) == 0:
            return 0
        if len(children) == 1:
            return sizes[next(iter(children)), v]
        assert len(children) >= 2
        q = 1e10
        rem = sum(sizes[c, v] for c in children)
        for c1, c2 in itertools.combinations(children, 2):
            q = min(q, rem + bin_costs[c1, v] + bin_costs[c2, v] - sizes[c1, v] - sizes[c2, v])
        return q

    for v, parent in subtrees_order:
        print('a', v, parent)
        children = set(adj[v]) - set([parent])
        sizes[v, parent] = 1 + sum(sizes[c, v] for c in children)
        bin_costs[v, parent] = hz(v, children)

    result = 1e10
    for v, children in adj.items():
        print('b', v)
        result = min(hz(v, children), result)

    print(result, file=fout)


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    cj.main(solve, __file__)
