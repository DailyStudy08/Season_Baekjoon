horse = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
monkey = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check(r, c, h, cnt):
    queue = []
    ground[r][c] = 1
    queue.append((r, c, h, cnt))
    while queue and len(result) < 5:
        r, c, k, cnt = queue.pop(0)
        if k:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not ground[nr][nc]:
                    if nr == H - 1 and nc == W - 1:
                        result.append(cnt + 1)
                    queue.append((nr, nc, k - 1, cnt + 1))
            for dr, dc in monkey:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not ground[nr][nc]:
                    if nr == H - 1 and nc == W - 1:
                        result.append(cnt + 1)
                    queue.append((nr, nc, k, cnt + 1))
        else:
            for dr, dc in monkey:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not ground[nr][nc]:
                    if nr == H - 1 and nc == W - 1:
                        result.append(cnt + 1)
                    queue.append((nr, nc, k, cnt + 1))


K = int(input())
W, H = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(H)]
visited = [[0] * W for _ in range(H)]
result = []
check(0, 0, K, 0)
if result:
    print(min(result))
else:
    print(-1)
