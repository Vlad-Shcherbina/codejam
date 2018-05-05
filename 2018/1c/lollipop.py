import sys
import random

T = int(input())
for case in range(1, T + 1):
    n = int(input())
    popularity = dict.fromkeys(range(n), 0)
    if n == -1:
        exit()
    for _ in range(n):
        len_pref, *pref = map(int, input().split())
        if len_pref == -1:
            exit()
        assert len_pref == len(pref)
        pref = [x for x in pref if x in popularity]
        for x in pref:
            popularity[x] += 1
        if pref:
            x = min(pref, key=popularity.get)
            print(x)
            del popularity[x]
        else:
            print(-1)
        sys.stdout.flush()
