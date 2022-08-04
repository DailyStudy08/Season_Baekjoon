N = int(input())
lst = []
for i in range(N):
    a = list(input().split())
    lst += [a]
b = sorted(lst, key=lambda x : int(x[0]))

for name in b:
    print(name[0], name[1])