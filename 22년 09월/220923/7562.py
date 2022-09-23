from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
d = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
# 8가지

def BFS(r, c):
    if r == r2 and c == c2:
        print(arr[r][c])
        return
    for i in range(8):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < I and 0 <= nc < I and not arr[nr][nc]:
            arr[nr][nc] = arr[r][c] + 1
            que.append((nr, nc))
    cr, cc = que.popleft()
    BFS(cr, cc)



T = int(input())
for _ in range(T):
    I = int(input())
    arr = [[0] * I for _ in range(I)]
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    que = deque()
    BFS(r1, c1)