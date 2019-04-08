import random

num_tests = int(input())
for case in range(num_tests):
    n = int(input())
    while True:
        a = random.randrange(1, n)
        if '4' not in str(a) + str(n - a):
            print('Case #{}: {} {}'.format(case + 1, a, n - a))
            break
