from collections import deque


def BFS(arr):
    result = 0
    while queue:
        r, c, result = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
                arr[nr][nc] = 1
                queue.append((nr, nc, result + 1))
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                result = -1
    return result


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j, 0))
print(BFS(arr))
