N, X = map(int, input().split())
lst = list(map(int, input().split()))
if max(lst) == 0:
    print('SAD')
else:
    result = sum(lst[:X])
    check = result
    cnt = 1
    for i in range(X, N):
        check -= lst[i - X]
        check += lst[i]
        if result < check:
            result = check
            cnt = 1
        elif result == check:
            cnt += 1
    print(result)
    print(cnt)