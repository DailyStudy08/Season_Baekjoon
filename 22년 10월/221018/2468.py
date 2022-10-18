def DFS(r, c):
    visited[n][m] = 1
    stack = []
    stack.append((r, c))
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > i and not visited[nr][nc]:
                visited[nr][nc] = 1
                stack.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(min(min(arr)) - 1, max(max(arr)) + 1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if arr[n][m] > i and not visited[n][m]:
                DFS(n, m)
                cnt += 1
    if cnt > result:
        result = cnt
print(result)
