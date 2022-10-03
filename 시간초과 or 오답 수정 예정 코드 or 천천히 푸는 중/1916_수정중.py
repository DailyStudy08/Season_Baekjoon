import sys
input = sys.stdin.readline


def dijk(S, E):
    check_idx = S
    queue = []
    queue.append(S)
    while queue:
        min_idx = 0
        min_value = 100001
        for i in range(1, N+1):
            if not visited[i] and arr[check_idx][i] < min_value:
                min_value = arr[check_idx][i]
                min_idx = i
        visited[min_idx] = 1
        for i in range(1, N+1):
            if not visited[i] and arr[min_idx][i] + min_value < arr[check_idx][i]:
                arr[check_idx][i] = arr[min_idx][i] + min_value
        check_idx = min_idx
    return arr[S][E]


N = int(input())
M = int(input())
arr = [[10000000000] * (N+1) for _ in range(N+1)]
for i in range(M):
    s, e, c = map(int, input().split())
    arr[s][e] = c
    if i < N + 1:
        arr[i][i] = 0
S, E = map(int, input().split())

print(dijk(S, E))