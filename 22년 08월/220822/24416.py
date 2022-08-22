import sys

def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    global cnt2
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

cnt1 = 0
cnt2 = 0

n = int(sys.stdin.readline())
fib(n)
fibonacci(n)
print(cnt1, cnt2)


#### 재귀 dp 연습용으로 풀었고... python3으로는 시간초과 나서 pypy3으로 제출했습니다.