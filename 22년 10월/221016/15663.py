def go(cnt):
    if cnt == M:
        check.add(tuple(result))
        return
    for i in range(N):
        if not visited[i]:
            result.append(num_lst[i])
            visited[i] = 1
            go(cnt + 1)
            result.pop()
            visited[i] = 0


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
check = set()
visited = [0] * N
result = []
go(0)
check = list(check)
check.sort()
for num in check:
    print(*num)
