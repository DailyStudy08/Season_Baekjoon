import sys
from collections import deque
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def BFS():
    width = 1
    while queue:
        r, c = queue.popleft()
        for d in delta:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                width += 1
                queue.append((nr, nc))
    return width


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            queue = deque()
            queue.append((i, j))
            width = BFS()
            if width > result:
                result = width
print(cnt)
print(result)
