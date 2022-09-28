def check(s, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i]:
            result.append(i + 1)
            visited[i] = 1
            check(s, cnt + 1)
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())
result = []
visited = [0] * N
check(0, 0)