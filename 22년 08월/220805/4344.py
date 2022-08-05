N = int(input())
for i in range(N):
    lst = []
    a,*b = map(int, input().split())
    s = sum(b)/a
    for el in b:
        if el > s:
            lst += [el]
    print(f'{len(lst) * 100 / a:.3f}%')