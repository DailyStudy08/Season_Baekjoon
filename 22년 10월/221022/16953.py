A, B = map(int, input().split())
visited = []
queue = []
cnt = 0
check = 0
queue.append((A, cnt))
while queue:
    num, cnt = queue.pop(0)
    if num == B:
        check = 1
        break
    num1 = num * 2
    num2 = num * 10 + 1
    if 0 <= num1 <= 1000000000:
        queue.append((num1, cnt+1))
    if 0 <= num2 <= 1000000000:
        queue.append((num2, cnt+1))
if not check:
    print(-1)
else:
    print(cnt + 1)
