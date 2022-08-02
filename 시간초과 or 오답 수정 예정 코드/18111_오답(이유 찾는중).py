import math
N,M,B = map(int, input().split())
m = []
c = 0
for i in range(N):
    m += [list(map(int, input().split()))]
for o in m:
    c += sum(o)
aver = round(c / (N * M))

l = [] #작은값
u = [] #큰값

for g in m:
    for s in g:
        if s < aver:
            l += [s]
        elif s > aver:
            u += [s]

lower = aver * len(l) - sum(l)
upper = sum(u) - aver * len(u)
if B + upper < lower:
    aver -=  math.ceil((lower - upper - B)/(N * M))
    for g in m:
        for s in g:
            if s < aver:
                l += [s]
            elif s > aver:
                u += [s]

    lower = aver * len(l) - sum(l)
    upper = sum(u) - aver * len(u)
    print(upper * 2 + lower * 1, aver)
else:
    print(upper * 2 + lower * 1, aver)