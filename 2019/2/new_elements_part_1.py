from fractions import Fraction

T = int(input())
for case in range(T):
    N = int(input())
    ws = []
    for _ in range(N):
        ws.append(tuple(map(int, input().split())))
    angles = set()
    has_zero = False
    for i in range(N):
        for j in range(i):
            dx = ws[i][0] - ws[j][0]
            dy = ws[i][1] - ws[j][1]
            if (dx, dy) == (0, 0):
                has_zero = True
                break
            dy = -dy
            if dx * dy >= 0:
                angles.add(Fraction(dx, dx + dy))
    angles.discard(0)
    angles.discard(1)
    result = len(angles) + 1
    if has_zero:
        result = 0
    print('Case #{}: {}'.format(case + 1, result))
