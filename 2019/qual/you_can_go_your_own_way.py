num_tests = int(input())
for case in range(num_tests):
    n = int(input())
    path = input()
    assert len(path) == 2 * n - 2
    path = path.replace('S', 't').replace('E', 'S').replace('t', 'E')
    print('Case #{}: {}'.format(case + 1, path))
