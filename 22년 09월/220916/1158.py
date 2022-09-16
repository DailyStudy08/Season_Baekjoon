# def jos(lst):
#     global cnt
#     cnt = (cnt + (K-1)) % len(lst)
#     a = lst.pop(cnt)
#     if lst:
#         print(a, end=', ')
#         jos(lst)
#     else:
#         print(a, end='')


# N, K = map(int, input().split())
# lst = [x for x in range(1, N+1)]
# print('<', end='')
# cnt = 0
# jos(lst)
# print('>')

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [x for x in range(1, N + 1)]
check = [0] * N
print('<', end='')
cnt = -1
for _ in range(N-1):
    for _ in range(K):
        cnt = (cnt + 1) % N
        while check[cnt]:
            cnt = (cnt + 1) % N
    if not check[cnt]:
        print(lst[cnt], end=', ')
        check[cnt] = 1
for i in range(N):
    if not check[i]:
        print(lst[i], end='')
print('>')