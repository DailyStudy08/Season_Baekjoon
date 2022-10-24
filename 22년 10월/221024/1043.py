def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x in true:
        parent[y] = x
    elif y in true:
        parent[x] = y
    else:
        parent[x] = y


N, M = map(int, input().split())
T, *true = map(int, input().split())
parent = [x for x in range(N + 1)]
result = []
for _ in range(M):
    P, *party = map(int, input().split())
    result.append(party)
    for i in range(1, P):
        union(party[0], party[i])
# print(result)
# print(parent)
cnt = 0
for part in result:
    for el in part:
        if find_set(el) in true:
            break
    else:
        cnt += 1
print(cnt)

