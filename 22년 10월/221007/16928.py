def BFS(start):
    queue = []
    queue.append(start)
    qdx = 0
    while qdx < len(queue):
        recent = queue[qdx]
        for i in range(1, 7):
            go = recent + i
            if go > 100:
                go = 100
            if arr[go]:
                if visited[arr[go]] > visited[recent] + 1:
                    visited[arr[go]] = visited[recent] + 1
                    queue.append(arr[go])
            else:
                if visited[go] > visited[recent] + 1:
                    visited[go] = visited[recent] + 1
                    queue.append(go)

        qdx += 1


N, M = map(int, input().split())
arr = [0] * 101
visited = [0, 0] + [100] * 99
for _ in range(N):
    x, y = map(int, input().split())
    arr[x] = y
for _ in range(M):
    x, y = map(int, input().split())
    arr[x] = y

BFS(1)
print(visited[100])