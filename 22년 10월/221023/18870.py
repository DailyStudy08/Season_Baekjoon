import sys
input = sys.stdin.readline


N = int(input())
X = list(map(int, input().split()))
X_sort = sorted(list(set(X)))
dx = {}
for i in range(len(X_sort)):
    dx[X_sort[i]] = i
for i in range(N):
    print(dx[X[i]], end=' ')
