import sys
input = sys.stdin.readline


# M, N = map(int, input().split())
# arr = []
# for i in range(M):
#     arr.append(list(map(int, input().split())))
#
# result = 0
# for i in range(M):
#     for j in range(i+1, M):
#         cnt = 0
#         check = True
#         for n in range(N):
#             for m in range(n+1, N):
#                 if arr[i][n] < arr[i][m] and arr[j][n] < arr[j][m]:
#                     cnt += 1
#                 elif arr[i][n] == arr[i][m] and arr[j][n] == arr[j][m]:
#                     cnt += 1
#                 elif arr[i][n] > arr[i][m] and arr[j][n] > arr[j][m]:
#                     cnt += 1
#                 else:
#                     check = False
#                     break
#             if not check:
#                 break
#         if cnt == N * (N-1) // 2:
#             result += 1
# print(result)

M, N = map(int, input().split())
universe = {}
for _ in range(M):
    lst = list(map(int, input().split()))
    temp = sorted(list(set(lst)))
    temp_dic = {}
    for i in range(len(temp)):
        temp_dic[temp[i]] = i
    check = tuple(temp_dic[lst[x]] for x in range(N))
    # print(check)
    if check in universe:
        universe[check] += 1
    else:
        universe[check] = 1

result = 0
for value in universe.values():
    if value > 1:
        result += value * (value - 1) // 2

print(result)
