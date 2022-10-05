import sys
input = sys.stdin.readline


def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x


# 이걸로 시간초과에서 벗어났는데 이거 차이가 좀 있나 생각에 빠짐...
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
parent = [x for x in range(N+1)]
arr = []
for _ in range(M):
    A, B, C = map(int, input().split())
    arr.append((C, A, B))

arr.sort()

mst = set()
idx = 0
result = 0
while len(mst) != N - 2:
    if find_set(arr[idx][1]) != find_set(arr[idx][2]):
        union(arr[idx][1], arr[idx][2])
        mst.add(arr[idx])
        result += arr[idx][0]
    idx += 1
print(result)
