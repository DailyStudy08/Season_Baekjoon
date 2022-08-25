A, B, V = map(int, input().split())
if V%(A-B) == 0:
    print(V//(A-B))
else:
    if (V-A)//(A-B) == 0:
        print(2)
    else:
        print((V-A)//(A-B)+1)