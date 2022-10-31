def BFS(s, cnt):
    queue = []
    queue.append((s, cnt))
    visited[s] = 0
    while K not in visited:
        s, cnt = queue.pop(0)
        if s + 1 not in visited and 0 <= s + 1 <= 100000:
            visited[s+1] = cnt + 1
            queue.append((s+1, cnt + 1))
        if s - 1 not in visited and 0 <= s - 1 <= 100000:
            visited[s-1] = cnt + 1
            queue.append((s-1, cnt + 1))
        if 2*s not in visited and 0 <= 2*s <= 100000:
            visited[2*s] = cnt + 1
            queue.append((2*s, cnt + 1))


N, K = map(int, input().split())
visited = {}
BFS(N, 0)
print(visited[K])
