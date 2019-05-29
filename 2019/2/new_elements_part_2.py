from fractions import Fraction
import math


def cf(x: Fraction):
    a = [None, None]
    p = [0, 1]
    q = [1, 0]
    i = 2
    while True:
        a.append(None)
        p.append(None)
        q.append(None)
        a[i] = math.floor(x)
        p[i] = a[i] * p[i - 1] + p[i - 2]
        q[i] = a[i] * q[i - 1] + q[i - 2]
        x -= a[i]
        if x == 0:
            break
        x = 1 / x
        i += 1
    return a, p, q


def best_approximations(x: Fraction):
    a, p, q = cf(x)
    for i in range(2, len(a) - 1):
        n = a[i + 1] // 2
        cp = n * p[i] + p[i - 1]
        cq = n * q[i] + q[i - 1]
        e1 = abs(x - Fraction(cp, cq))
        e2 = abs(x - Fraction(p[i], q[i]))
        if e1 < e2:
            yield cp, cq
        n1 = (a[i + 1] + 2) // 2
        n2 = a[i + 1] + 1
        for n in range(n1, n2):
            yield n * p[i] + p[i - 1], n * q[i] + q[i - 1]


from fractions import Fraction

T = int(input())
for case in range(T):
    N = int(input())
    ws = []
    for _ in range(N):
        ws.append(tuple(map(int, input().split())))
    lower = Fraction(0)
    upper = Fraction(1)
    for i in range(N):
        for j in range(i):
            dx = ws[i][0] - ws[j][0]
            dy = ws[i][1] - ws[j][1]
            if dy > 0:
                if dx < 0:
                    lower = max(lower, Fraction(-dx, (dy - dx)))
            elif dy < 0:
                if dx > 0:
                    upper = min(upper, Fraction(dx, (dx - dy)))
                else:
                    lower = 0
                    upper = 0
            else:
                if dx <= 0:
                    lower = 0
                    upper = 0

    lower_b = lower.numerator
    lower_a = lower.denominator - lower.numerator

    upper_b = upper.numerator
    upper_a = upper.denominator - upper.numerator
    # print(lower_b, lower_a, '...', upper_b, upper_a)

    result = 'zzz'
    if lower >= upper:
        result = 'IMPOSSIBLE'
    else:
        if upper_a == 0:
            a = 1
            b = lower_b // lower_a + 1
            result = '{} {}'.format(a, b)
        else:
            lower = Fraction(lower_b, lower_a)
            upper = Fraction(upper_b, upper_a)
            x = (lower + upper) / 2
            threshold = (upper - lower) / 2
            for bb, aa in best_approximations(x):
                d = abs(Fraction(bb, aa) - x)
                if d < threshold:
                    bb = aa * lower_b // lower_a + 1
                    result = '{} {}'.format(aa, bb)
                    break
            else:
                assert False


    print('Case #{}: {}'.format(case + 1, result))
