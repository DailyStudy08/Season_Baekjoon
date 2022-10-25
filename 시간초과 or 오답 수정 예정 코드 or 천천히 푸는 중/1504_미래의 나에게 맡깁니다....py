def check(s):
    for i in range(1, N+1):
        if arr[s][i]:
            

N, E = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(E):
    s, e, c = map(int, input().split())
    arr[s][e] = c
    arr[e][s] = c
v1, v2 = map(int, input().split())

queue = []
check(1)