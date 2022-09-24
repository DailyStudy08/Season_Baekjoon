def check(num):
    global result
    if num >= n:
        if num == n:
            result += 1
        return
    for i in range(1, 4):
            check(num + i)



t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    check(0)
    print(result)