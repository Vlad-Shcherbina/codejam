T = int(input())
for _ in range(T):
    A = int(input())
    c = {(i, j): 0 for i in range(2, 15) for j in range(2, 14)}
    q = set()
    while True:
        i, j = min(c, key=c.get)
        print(i, j, flush=True)
        i, j = map(int, input().split())
        if i == j == 0:
            break
        elif i == j == -1:
            exit()
        if (i, j) not in q:
            q.add((i, j))
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if (ii, jj) in c:
                        c[ii, jj] += 1
