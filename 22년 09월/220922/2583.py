import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):                                                                          # 라고 적긴 했는데 이거 dfs인듯
    global cnt
    visited[r][c] = 1
    cnt += 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < M and 0 <= nc < N and not arr[nr][nc] and not visited[nr][nc]:
            bfs(nr, nc)


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] += 1
result = []
for i in range(M):
    for j in range(N):
        cnt = 0
        if not arr[i][j] and not visited[i][j]:
            bfs(i, j)
            result.append(cnt)
result = sorted(result)
print(len(result))
print(*result)
