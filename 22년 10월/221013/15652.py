def check(s, cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(s, N + 1):
        result.append(i)
        check(i, cnt + 1)
        result.pop()


N, M = map(int, input().split())
result = []
check(1, 0)