d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 상 하 좌 우


def DFS(r, c):
    global all
    for de in d:
        nr = r + de[0]
        nc = c + de[1]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = cnt
            all += 1
            DFS(nr, nc)



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            visited[i][j] = cnt
            all = 1
            DFS(i, j)
            result.append(all)
print(cnt)
result.sort()
for el in result:
    print(el)
