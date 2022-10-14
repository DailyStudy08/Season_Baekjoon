def check(cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i]:
            result.append(num[i])
            visited[i] = 1
            check(cnt + 1)
            result.pop()
            visited[i] = 0


N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []
visited = [0] * N
check(0)
