d = {0: (-1, 0), 1: (0, 1), 2:(1, 0), 3: (0, -1)}


def DFS(r, c, de):
    global cnt
    if not arr[r][c] and not visited[r][c]:
        visited[r][c] = 1
        cnt += 1
    for i in range(4):
        nr = r + d[(de - i) % 4][0]
        nc = c + d[(de - i) % 4][1]
        if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc] and not visited[nr][nc]:
            DFS(nr, nc, (de + i) % 4)




N, M = map(int, input().split())
r, c, de = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
DFS(r, c, de)
print(cnt)
