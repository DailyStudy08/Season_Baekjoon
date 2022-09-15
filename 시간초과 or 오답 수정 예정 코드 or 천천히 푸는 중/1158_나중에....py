def jos(lst):
    global cnt
    cnt = (cnt + (K-1)) % len(lst)
    a = lst.pop(cnt)
    if lst:
        print(a, end=', ')
        jos(lst)
    else:
        print(a, end='')


N, K = map(int, input().split())
lst = [x for x in range(1, N+1)]
print('<', end='')
cnt = 0
jos(lst)
print('>')