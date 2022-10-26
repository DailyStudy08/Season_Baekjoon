def check(idx, start, end, cnt):
    global result
    if cnt > result:
        result = cnt
    for i in range(idx, N):
        s, e, c = lst[i]
        if s > end and e < N + 1:
            check(i + 1, s, e, cnt + c)


N = int(input())
lst = []
result = 0
for i in range(1, N+1):
    day, cost = map(int, input().split())
    lst.append((i, i + day - 1, cost))
# print(lst)
check(0, 0, 0, 0)
print(result)