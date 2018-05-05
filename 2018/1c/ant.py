def pareto(xs):
    xs = sorted(xs, reverse=True)
    result = []
    prev_y = float('-inf')
    for xy in xs:
        y = xy[1]
        if y > prev_y:
            result.append(xy)
            prev_y = y
    return result

T = int(input())
for case in range(T):
    n = int(input())
    ws = list(map(int, input().split()))
    assert n == len(ws)
    front = [(0, 10**10)]
    for w in reversed(ws):
        new_front = front[:]
        for x, y in front:
            if y >= w:
                y = min(6 * w, y - w)
                new_front.append((x + 1, y))
        front = pareto(new_front)
    print('Case #{}: {}'.format(case + 1, max(front)[0]))
