def lotto(s, e, cnt):
    if cnt == 6:
        print(*result)
        return
    for i in range(s, e):
        result.append(lst[i])
        lotto(i + 1, e + 1, cnt+1)
        result.pop()



a = input()
while a != '0':
    k, *lst = map(int, a.split())
    result = []
    lotto(0, k - 5, 0)
    print()
    a = input()