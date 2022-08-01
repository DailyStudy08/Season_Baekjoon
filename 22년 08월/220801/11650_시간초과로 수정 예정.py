N = int(input())
lst = []
for i in range(N):
    a = list(map(int, input().split()))
    lst += [a]
ans = sorted(lst)
for o in ans:
    print(o[0], o[1])