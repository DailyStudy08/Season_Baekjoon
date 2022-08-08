N,M = map(int, input().split())
a = set()
b = set()
for i in range(N):
    a.add(input())
for j in range(M):
    b.add(input())
c = a & b
print(len(c))
for k in sorted(list(c)):
    print(k)