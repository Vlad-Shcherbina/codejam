import itertools

T = int(input())
for case in range(T):
    N, L = map(int, input().split())
    words = set()
    letters = [set() for _ in range(L)]
    for _ in range(N):
        word = input()
        assert len(word) == L
        for i, c in enumerate(word):
            letters[i].add(c)
        words.add(word)
    result = '-'
    for word in itertools.product(*letters):
        word = ''.join(word)
        if word not in words:
            result = word
            break
    print('Case #{}: {}'.format(case + 1, result))
