import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(R):
    global cnt
    stack.append(R)
    while stack:
        go = stack.pop()
        if not visited[go]:
            visited[go] = 1
            cnt += 1
            result[go] = cnt
            for i in arr[go]:
                if arr[i] and not visited[i]:
                    dfs(i)



N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
for a in arr:
    a.sort()
stack = []
cnt = 0
result = [0] * (N+1)
# print(arr)
dfs(R)
for i in range(1, N+1):
    print(result[i])