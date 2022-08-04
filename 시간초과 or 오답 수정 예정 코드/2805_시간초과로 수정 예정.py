N,M = map(int, input().split())
lst = list(map(int, input().split()))
wood = sorted(lst)
a = wood[-1] -1
c = 0
while c < M:
    for w in wood:
        if w - a > 0:
            c += 1
    a -= 1
print(a + 1)