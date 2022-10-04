from collections import deque


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    cnt = 0
    while queue:
        start = queue.popleft()
        for el in arr[start]:
            if not visited[el]:
                visited[el] = 1
                cnt += 1
                queue.append(el)
    # print(visited)
    print(cnt)



# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     arr = [[] for _ in range(N+1)]
#     visited = [0] * (N+1)
#     for _ in range(M):
#         a, b = map(int, input().split())
#         arr[a].append(b)
#         arr[b].append(a)
#     print(N-1)
# 최소 신장 트리에서 간선 수는 노드 -1개니까...