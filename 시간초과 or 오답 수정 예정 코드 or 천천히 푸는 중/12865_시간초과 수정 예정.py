import sys
input = sys.stdin.readline


def check(s, w, cnt):
    global result
    if result < cnt:
        result = cnt
    for i in range(s, N):
        if w - bag[i][0] >= 0:
            check(i+1, w - bag[i][0], cnt + bag[i][1])


N, K = map(int, input().split())
bag = []
result = 0
for _ in range(N):
    W, V = map(int, input().split())
    bag.append((W, V))
check(0, K, 0)
print(result)
