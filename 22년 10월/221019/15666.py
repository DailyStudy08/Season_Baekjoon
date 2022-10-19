def check(cnt):
    if cnt == M:
        num_set.add(tuple(sorted(result)))
        return
    for i in range(N):
        result.append(num[i])
        check(cnt + 1)
        result.pop()


N, M = map(int, input().split())
num = list(map(int, input().split()))

num_set = set()
result = []
check(0)
num_list = list(num_set)
num_list.sort()
for n in num_list:
    print(*n)
