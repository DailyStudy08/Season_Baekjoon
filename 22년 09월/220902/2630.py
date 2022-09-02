def check(N, num1, num2):
    global result1, result2
    if not N:
        if arr[num1][num2]:
            result1 += 1
        else:
            result2 += 1
    else:
        for i in range(num1, num1 + N//2 + 1, N//2):
            for j in range(num2, num2 + N//2 + 1, N//2):
                cnt1 = cnt2 = 0
                for a in range(N//2):
                    for b in range(N//2):
                        if arr[i+a][j+b]:
                            cnt1 += 1
                        else:
                            cnt2 += 1
                if cnt1 == N//2 * N//2:
                    result1 += 1
                elif cnt2 == N//2 * N//2:
                    result2 += 1
                else:
                    check(N//2, i, j)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result1 = 0
result2 = 0
check1 = check2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            check1 += 1
        else:
            check2 += 1
if check1 == N * N:
    result1 = 1
elif check2 == N * N:
    result2 = 1
else:
    check(N, 0, 0)
print(result2)
print(result1)
