N = int(input())
a = list(map(int, input().split()))
cnt = 0
for num in a:
    lst = []
    for i in range(1,num+1):
        if num % i == 0:
            lst += [i]
    if len(lst) == 2:
                cnt += 1
print(cnt)