N, M = map(int, input().split())
dic1 = {}
dic2 = {}
for i in range(1, N+1):
    a = input()
    dic1[i] = a
    dic2[a] = i
for j in range(M):
    a = input()
    if a in dic2:
        print(dic2[a])
    else:
        print(dic1[int(a)])


### pypy3으로 통과