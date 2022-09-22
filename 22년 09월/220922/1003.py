def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


T = int(input())
for _ in range(T):
    memo = {}
    memo[0] = (1, 0)
    memo[1] = (0, 1)
    for i in range(2, 42):
        memo[i] = (memo[i - 1][0] + memo[i - 2][0], memo[i - 1][1] + memo[i - 2][1])
    n = int(input())
    print(*memo[n])
