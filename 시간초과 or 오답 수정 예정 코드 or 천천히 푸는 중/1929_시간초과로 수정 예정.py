M, N = map(int, input().split())
for i in range(M, N+1):
    num = []
    for j in range(1, i+1):
        if i % j == 0:
            num.append(j)
    if len(num) == 2:
        print(num[-1])
