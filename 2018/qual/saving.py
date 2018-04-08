n = int(input())

for case in range(1, n + 1):
    d, cmd = input().split()
    d = int(d)

    dmg = 0
    xs = [0]
    for c in cmd:
        if c == 'S':
            xs[-1] += 1
            dmg += 2**(len(xs) - 1)
        elif c == 'C':
            xs.append(0)

    result = 0
    for i in reversed(range(1, len(xs))):
        w = 2**(i - 1)
        for j in range(xs[i]):
            if dmg <= d:
                break
            dmg -= w
            result += 1
            xs[i - 1] += 1

    if dmg > d:
        result = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(case, result))