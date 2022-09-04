import sys
sys.setrecursionlimit(1000000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def miro(r, c):
    if not visited[r][c]:
        visited[r][c] = 1
    if visited[N-1][M-1]:
        print(visited[N-1][M-1])
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            stack.append([nr, nc])
    a, b = stack.pop(0)
    miro(a, b)


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
stack = []
miro(0, 0)
