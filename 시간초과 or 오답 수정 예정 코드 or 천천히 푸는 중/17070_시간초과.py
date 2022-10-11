import sys
sys.stdin.readline

line_shape = {
    0: [[(0, 1), (0, 1)], [], [(0, 1), (1, 1)]],    # 가로
    1: [[], [(1, 0), (1, 0)], [(1, 0), (1, 1)]],    # 세로
    2: [[(1, 1), (0, 1)], [(1, 1), (1, 0)], [(1, 1), (1, 1)]]     # 대각선
}


def DFS(r1, c1, r2, c2, line):
    global result
    stack = []
    stack.append((r1, c1, r2, c2, line))
    while stack:
        r, c, x, y, l = stack.pop()
        if x == N -1 and y == N -1:
            result += 1
        for i in range(len(line_shape[l])):
            if line_shape[l][i]:
                nr, nc = r + line_shape[l][i][0][0], c + line_shape[l][i][0][1]
                nx, ny = x + line_shape[l][i][1][0], y + line_shape[l][i][1][1]
                if nx < N and ny < N and not home[nx][ny]:
                    if i == 2:
                        if not home[nr][ny] and not home[nx][nc]:
                            stack.append((nr, nc, nx, ny, i))
                    else:
                        stack.append((nr, nc, nx, ny, i))


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
result = 0
DFS(0, 0, 0, 1, 0)
print(result)
