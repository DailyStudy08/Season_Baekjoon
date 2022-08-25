def dfs(V):
    stack.append(V)
    # top = stack[-1]
    print(top, end=' ')
    visited[V] = 1
    while stack:
        top = stack.pop()
        for i in range(1, N+1):
            if graph[top][i] and not visited[i]:
                  stack.append(i)
                  visited[i] = 1
                # break
        # else:
        #     stack.pop()
        #     return


# def bfs(V):
#     queue = []




N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
stack = []
visited = [0] * (N+1)
dfs(V)
# bfs(V)