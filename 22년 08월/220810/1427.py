lst = list(map(int, input()))

for i in range(len(lst)-1, 0, -1):
    for j in range(0, i):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

for k in lst:
    print(k, end='')