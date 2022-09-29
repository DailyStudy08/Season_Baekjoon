def check(s, c):
    if c == M:
        print(*result)
    for i in range(s, N):
        if not visited[i]:
            visited[i] = 1
            result.append(num[i])
            check(i+1, c+1)
            visited[i] = 0
            result.pop()


N, M = map(int, input().split())
num = [x for x in range(1, N+1)]
result = []
visited = [0] * N
check(0, 0)
