a = sorted(list(map(int, input().split())))
if a[0] == a[1]:
    if a[0] == a[2]:
        print(10000 + 1000 * a[0])
    else:
        print(1000 + 100 * a[0])
elif a[1] == a[2]:
    print(1000 + 100 * a[1])
else:
    print(100 * a[2])