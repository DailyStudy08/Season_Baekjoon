import sys
input = sys.stdin.readline


N = int(input())
X = list(map(int, input().split()))
X_sort = sorted(X)
dx = {}
for i in range(N):
    if X_sort[i] not in dx:
        dx[X_sort[i]] = 1
answer = {}
for i in range(N):
    cnt = 0
    if X[i] not in answer:
        for j in dx:
            if j < X[i]:
                cnt += 1
            else:
                break
        answer[X[i]] = cnt
    else:
        cnt = answer[X[i]]
    print(cnt, end=' ')
