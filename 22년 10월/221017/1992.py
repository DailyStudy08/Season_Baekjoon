def check(s, e, n):
    cnt1 = cnt2 = 0
    for i in range(s, s + n):
        for j in range(e, e + n):
            if arr[i][j]:
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 and cnt2:
                print('(', end='')
                for k in range(s, s + n, n//2):
                    for l in range(e, e + n, n//2):
                        check(k, l, n//2)
                print(')', end='')
                return
    else:
        if cnt1 and not cnt2:
            print(1, end='')
        elif not cnt1 and cnt2:
            print(0, end='')


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
check(0, 0, N)