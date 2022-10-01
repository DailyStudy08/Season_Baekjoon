def BFS(r):
    queue = [r]
    distance = [0] * (N+1)
    while queue:
        r = queue.pop(0)
        for c in range(N+1):
            if arr[r][c] and not visited[c]:
                queue.append(c)
                visited[c] = 1
                distance[c] = distance[r] + 1
    return sum(distance)


N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
result = 500000000
result_idx = 0
for i in range(1, N+1):
    visited = [1] + [0] * N
    cnt = BFS(i)
    if cnt < result:
        result = cnt
        result_idx = i
print(result_idx)