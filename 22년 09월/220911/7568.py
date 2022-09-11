N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
# print(lst)
arr = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1
    arr.append([cnt, i])
# print(arr)
for i in range(N):
    print(arr[i][0] + 1, end=' ')
