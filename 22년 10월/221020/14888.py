import math
import sys
input = sys.stdin.readline


def check(n, cnt):
    global result1, result2
    if cnt == n:
        calculator = A[:]
        for i in range(n):
            if cal_lst[cal_idx[i]] == '+':
                calculator[i+1] = calculator[i] + calculator[i+1]
            elif cal_lst[cal_idx[i]] == '-':
                calculator[i+1] = calculator[i] - calculator[i+1]
            elif cal_lst[cal_idx[i]] == '*':
                calculator[i+1] = calculator[i] * calculator[i+1]
            elif cal_lst[cal_idx[i]] == '/':
                calculator[i+1] = math.trunc(calculator[i] / calculator[i+1])
        if result1 < calculator[-1]:
            result1 = calculator[-1]
        if result2 > calculator[-1]:
            result2 = calculator[-1]
        return
    for i in range(n):
        if i not in cal_idx:
            cal_idx.append(i)
            check(n, cnt + 1)
            cal_idx.pop()


N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split()))
cal_lst = []
result1 = -1000000001
result2 = 1000000001
while cal[0] != 0:
    cal_lst.append('+')
    cal[0] -= 1
while cal[1] != 0:
    cal_lst.append('-')
    cal[1] -= 1
while cal[2] != 0:
    cal_lst.append('*')
    cal[2] -= 1
while cal[3] != 0:
    cal_lst.append('/')
    cal[3] -= 1
cal_idx = []
check(len(cal_lst), 0)
print(result1)
print(result2)