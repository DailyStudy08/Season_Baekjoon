import sys
sys.setrecursionlimit(9999999)


def check(s, e, cnt, money):
    global result
    global go
    if cnt >= result:
        return
    if money > K:
        return
    elif money == K:
        if cnt < result:
            result = cnt
            go = False
            return
    for i in range(e - 1, s - 1, -1):
        check(s, e, cnt + 1, money + coins[i])
        if not go:
            break


N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append((int(input())))
result = K // coins[0]
go = True
check(0, N, 0, 0)
print(result)