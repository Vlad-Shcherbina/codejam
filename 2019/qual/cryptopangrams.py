def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num_tests = int(input())
for case in range(num_tests):
    n, L = map(int, input().split())
    xs = list(map(int, input().split()))

    primes = set()
    for x, y in zip(xs, xs[1:]):
        if x != y:
            t = gcd(x, y)
            primes.add(t)
            primes.add(x // t)
            primes.add(y // t)
    assert len(primes) == 26
    primes = sorted(primes)
    assert primes[-1] <= n

    first_factors = {p for p in primes if xs[0] % p == 0}
    for f in first_factors:
        result = chr(65 + primes.index(f))
        for x in xs:
            if x % f:
                break
            f = x // f
            result += chr(65 + primes.index(f))
        else:
            break
    else:
        assert False
    print('Case #{}: {}'.format(case + 1, result))
