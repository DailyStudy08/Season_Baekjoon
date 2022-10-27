import sys
sys.setrecursionlimit(99999999)

def dfs(r,  c):
    global farm_wolf
    global farm_sheep
    visited[r][c] = 1
    if farm[r][c] == 'o':
        farm_sheep += 1
    elif farm[r][c] == 'v':
        farm_wolf += 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and farm[nr][nc] != '#' and not visited[nr][nc]:
            dfs(nr, nc)


R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]
sheep, wolf = 0, 0
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if farm[i][j] != '#' and not visited[i][j]:
            farm_sheep, farm_wolf = 0, 0
            dfs(i, j)
            if farm_sheep > farm_wolf:
                sheep += farm_sheep
            else:
                wolf += farm_wolf
print(sheep, wolf)