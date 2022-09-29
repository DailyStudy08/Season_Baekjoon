import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(N):
    for j in range(N):
        lst.append((i, j))
a = 0
for r, c in lst:
    queue = []
    visited = [[0] * N for _ in range(N)]
    queue.append((r, 0))
    qdx = 0
    result = 0
    while qdx < len(queue):
        ar, cnt = queue[qdx]
        if cnt > 0 and ar == c:
            result = 1
            break
        for k in range(N):
            if arr[ar][k] and not visited[ar][k]:
                visited[ar][k] = 1
                queue.append((k, cnt + 1))
        qdx += 1
    a += 1
    print(result, end=' ')
    if a != 0 and a % N == 0:
        print()
