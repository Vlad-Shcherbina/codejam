from __future__ import print_function
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))
import cj


def solve(fin, fout, only_read):
    n, m = map(int, next(fin).split())
    zips = []
    for _ in range(n):
        zips.append(next(fin).strip())
    assert all(len(z) == 5 for z in zips)
    assert len(set(zips)) == len(zips)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        i, j = map(int, next(fin).split())
        adj[i - 1].append(j - 1)
        adj[j - 1].append(i - 1)
    if only_read:
        return

    def reachable(starts, allowed):
        visited = set(starts)
        worklist = list(starts)
        while worklist:
            v = worklist.pop()
            for w in adj[v]:
                if w in allowed and w not in visited:
                    visited.add(w)
                    worklist.append(w)
        return visited

    start = zips.index(min(zips))
    stack = [start]
    visited = {start}

    path = zips[start]

    for _ in range(n - 1):
        best_candidate = None
        best_zip = '99999999'
        for i, v in enumerate(stack):
            for w in adj[v]:
                if w in visited:
                    continue
                possible = reachable(
                    stack[:i + 1] + [w], set(range(n)) - visited)
                if possible | visited == set(range(n)):
                    if zips[w] < best_zip:
                        best_zip = zips[w]
                        best_candidate = i, w

        assert best_candidate is not None
        i, v = best_candidate
        assert v not in visited
        assert v in adj[stack[i]]
        stack = stack[:i + 1] + [v]
        visited.add(v)
        path += best_zip

    print(path, file=fout)


if __name__ == '__main__':
    cj.main(solve, __file__)
