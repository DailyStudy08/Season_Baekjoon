import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(num):
    if not visited[num]:
        visited[num] = 1
        if line[num]:
            for i in range(len(line[num])):
                if line[num][i]:
                    dfs(line[num][i])

N, M = map(int, input().split())
visited = [0] * (N+1)
line = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)   