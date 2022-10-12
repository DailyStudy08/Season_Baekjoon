import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


def DFS(r, c):
    visited[r][c] = 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] and not visited[nr][nc]:
            DFS(nr, nc)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)