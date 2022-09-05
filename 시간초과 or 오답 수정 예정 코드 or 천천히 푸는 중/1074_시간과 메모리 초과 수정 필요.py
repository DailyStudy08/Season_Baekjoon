def number(a, b, N):
    global result
    if N <= 1:
        for i in range(b, b + 2**N):
            for j in range(a, a + 2**N):
                arr[i][j] = result
                if i == r and j == c:
                    print(result)
                result += 1
    else:
        for k in range(b, b + 2**N, 2**(N-1)):
            for l in range(a, a + 2**N, 2**(N-1)):
                number(l, k, N-1)


N, r, c = map(int, input().split())
arr = [[0] * 2 ** N for _ in range(2 ** N)]
result = 0
number(0, 0, N)
