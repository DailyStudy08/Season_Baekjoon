import sys

arr = [[0] * 100 for _ in range(100)]
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(100):
        for j in range(100):
            for n in range(a-1, a+9):
                for m in range(b-1, b+9):
                    arr[n][m] = 1
n = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            n += 1
print(n)

# 아래의 코드로 pypy3으로 제출하였습니다....................................

# arr = [[0] * 100 for _ in range(100)]
# N = int(input())
# for _ in range(N):
#     a, b = map(int, input().split())
#     for i in range(100):
#         for j in range(100):
#             for n in range(a-1, a+9):
#                 for m in range(b-1, b+9):
#                     arr[n][m] = 1
# n = 0
# for i in range(100):
#     for j in range(100):
#         if arr[i][j] == 1:
#             n += 1
# print(n)