def find_set(x):
    while x != parents[x]:
        if parents[x] in lst:
            lst.append(x)
        x = parents[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


C = int(input())
lst = [1]
parents = [x for x in range(C+1)]
connect = int(input())
for _ in range(connect):
    x, y = map(int, input().split())
    union(x, y)

cnt = 0
for i in range(2, C+1):
    if parents[i] in lst:
        cnt += 1
print(lst)
print(cnt)