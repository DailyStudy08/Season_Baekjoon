while True:
    t = map(int, input().split())
    a,b,c = sorted(t)
    if a != 0:
        if a**2 + b**2 == c**2:
            print('right')
        else:
            print('wrong')
    elif a == 0 and b == 0 and c ==0:
        break
    else:
        print('wrong')