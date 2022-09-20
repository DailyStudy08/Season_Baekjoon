import sys
sys.setrecursionlimit(10000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check(r, c, st):
    if not visited[r][c]:
        visited[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == st and not visited[nr][nc]:
                check(nr, nc, st)


def check2(r, c, st):
    if not visited2[r][c]:
        visited2[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == st and not visited2[nr][nc]:
                check2(nr, nc, st)


RGB_dict = {'R': 0, 'G': 0, 'B': 0}
N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            check(i, j, arr[i][j])
            RGB_dict[arr[i][j]] += 1
# print(RGB_dict)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
# print(arr)
RGB_dict2 = {'R': 0, 'B': 0}
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            check2(i, j, arr[i][j])
            RGB_dict2[arr[i][j]] += 1
# print(RGB_dict2)
print(RGB_dict['R'] + RGB_dict['G'] + RGB_dict['B'], RGB_dict2['R'] + RGB_dict2['B'])