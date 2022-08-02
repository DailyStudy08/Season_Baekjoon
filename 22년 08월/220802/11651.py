N = int(input())
lst = []
for i in range(N):
    a = list(map(int, input().split()))
    lst += [a]
ans = sorted(lst, key = lambda x : (x[1], x[0]))
for o in ans:
    print(o[0], o[1])