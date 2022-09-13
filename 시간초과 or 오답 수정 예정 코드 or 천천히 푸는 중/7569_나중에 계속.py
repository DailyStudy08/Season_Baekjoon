M, N, H = map(int, input().split())
arr = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    arr.append(temp)
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
print(visited)

dh = [0, 0, 0, 0, -1, 1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
for i in range(H):
    for j in range(N):
        for k in range(M):
            for l in range(6):
                arr[i+dh]
