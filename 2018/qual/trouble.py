T = int(input())
for case in range(T):
    n = int(input())
    xs = list(map(int, input().split()))
    assert len(xs) == n
    xs[::2] = sorted(xs[::2])
    xs[1::2] = sorted(xs[1::2])
    result = 'OK'
    for i in range(len(xs) - 1):
        if xs[i] > xs[i + 1]:
            result = i
            break
    print('Case #{}: {}'.format(case + 1, result))