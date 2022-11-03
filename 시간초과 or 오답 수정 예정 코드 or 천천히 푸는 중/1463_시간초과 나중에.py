def check(n):
    global cnt
    q = []
    q.append((n, 0))
    while q:
        num, c = q.pop(0)
        if num == 1:
            cnt = c
            break
        if not num % 3 and num % 3 >= 0:
            q.append((num // 3, c + 1))
        if not num % 2 and num % 2 >= 0:
            q.append((num // 2, c + 1))
        if num - 1 >= 0:
            q.append((num - 1, c + 1))


N = int(input())
cnt = 0
check(N)
print(cnt)
