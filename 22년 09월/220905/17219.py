import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = {}
for _ in range(N):     # 여기서 바보짓 해서 런타임 에러가 난 거였다...
    a, b = sys.stdin.readline().rstrip().split()
    arr[a] = b

for _ in range(M):
    c = sys.stdin.readline().rstrip()
    print(arr[c])