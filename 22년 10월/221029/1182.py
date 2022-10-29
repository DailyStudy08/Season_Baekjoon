def check(s, e, cnt):
    global result
    if cnt == e:
        if sum(nums) == S:
            result += 1
    for i in range(s, N):
        nums.append(num_lst[i])
        check(i+1, e, cnt + 1)
        nums.pop()


N, S = map(int, input().split())
num_lst = list(map(int, input().split()))
result = 0
nums = []
for i in range(1, N + 1):
    check(0, i, 0)
print(result)
