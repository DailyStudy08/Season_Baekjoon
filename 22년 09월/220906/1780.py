import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def number(num):
    global result1, result2, result3
    for i in range(N):
        for j in range(N):
            if arr[i][j] != num:
                check(N, 0, 0)
                return
    if arr[0][0] == -1:
        result1 += 1
        return
    elif arr[0][0] == 0:
        result2 += 1
        return
    else:
        result3 += 1
        return


def NNcheck(N, i, j):
    global cnt1, cnt2, cnt3
    for a in range(N):
        for b in range(N):
            if arr[i + a][j + b] == -1:
                if cnt2 or cnt3:
                    check(N, i, j)
                    return
                cnt1 += 1
            elif not arr[i + a][j + b]:
                if cnt1 or cnt3:
                    check(N, i, j)
                    return
                cnt2 += 1
            else:
                if cnt1 or cnt2:
                    check(N, i, j)
                    return
                cnt3 += 1


def check(N, num1, num2):
    global result1, result2, result3, cnt1, cnt2, cnt3
    if not N:
        if arr[num1][num2] == -1:
            result1 += 1
        elif not arr[num1][num2]:
            result2 += 1
        else:
            result3 += 1
    else:
        for i in range(num1, num1+N, N//3):
            for j in range(num2, num2+N, N//3):
                cnt1 = cnt2 = cnt3 = 0
                NNcheck(N//3, i, j)
                if cnt1 == N//3 * N//3:
                    result1 += 1
                elif cnt2 == N//3 * N//3:
                    result2 += 1
                elif cnt3 == N//3 * N//3:
                    result3 += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result1 = result2 = result3 = 0
num = arr[0][0]
cnt1 = cnt2 = cnt3 = 0
number(num)

print(result1)
print(result2)
print(result3)
