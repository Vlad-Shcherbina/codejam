from math import sqrt

T = int(input())
for case in range(T):
    a = float(input())
    y = a / sqrt(3)
    x = sqrt(1 - y * y)

    c = x * sqrt(2 / 3) + y * sqrt(1 / 3)
    s = y * sqrt(2 / 3) - x * sqrt(1 / 3)

    z1 = sqrt(1 / 8)
    x1 = z1 * c
    y1 = z1 * s

    print('Case #{}:'.format(case + 1))
    print(x1, y1, z1)
    print(x1, y1, -z1)
    print(-s / 2, c / 2, 0)
