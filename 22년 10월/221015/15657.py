def check(s, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(s, N):
        result.append(num[i])
        check(i, cnt + 1)
        result.pop()


N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []
check(0, 0)
