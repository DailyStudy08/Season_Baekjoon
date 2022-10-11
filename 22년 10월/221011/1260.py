def dfs(V):
    print(V, end=' ')
    visited1[V] = 1
    for i in range(1, N+1):
        if graph[V][i] and not visited1[i]:
            dfs(i)


def bfs(V):
    queue = []
    queue.append(V)
    visited2[V] = 1
    while queue:
        rear = queue.pop(0)
        print(rear, end=' ')
        for i in range(1, N + 1):
            if graph[rear][i] and not visited2[i]:
                queue.append(i)
                visited2[i] = 1


N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)
dfs(V)
print()
bfs(V)