def check(s, e, cnt):
    if cnt == M:
        print(*num_lst)
        return
    for i in range(s, e):
        num_lst.append(num[i])
        check(s, e, cnt + 1)
        num_lst.pop()


N, M = map(int, input().split())
num = [x for x in range(1, N + 1)]
num_lst = []
check(0, N, 0)