tc = int(input())
for i in range(tc):
    a= input()
    c = 0
    b = 0
    for o in range(0, len(a)):
        if a[o] == 'O':
            b += 1
            c += b
        else:
            b = 0
    print(c)
