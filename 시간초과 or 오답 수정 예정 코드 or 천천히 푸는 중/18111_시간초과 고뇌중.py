# import math
# N,M,B = map(int, input().split())
# m = []
# c = 0
# for i in range(N):
#     m += [list(map(int, input().split()))]
# for o in m:
#     c += sum(o)
# aver = round(c / (N * M))      # 평균으로 접근 하는 방식 저도 처음엔 그렇게 생각했는데 ..  높은 층이 아닌 시간이 우선순위라서 잘 하기 어려운것 같습니다.

# l = [] #작은값
# u = [] #큰값

# for g in m:
#     for s in g:
#         if s < aver:
#             l += [s]
#         elif s > aver:
#             u += [s]

# lower = aver * len(l) - sum(l)
# upper = sum(u) - aver * len(u)
# if B + upper < lower:
#     aver -=  math.ceil((lower - upper - B)/(N * M))   # 평균이 최선이 아닐 수가 있어서 문제점이 있을 가능성이 있습니다.
#     for g in m:
#         for s in g:
#             if s < aver:
#                 l += [s]
#             elif s > aver:
#                 u += [s]

#     lower = aver * len(l) - sum(l)          
#     upper = sum(u) - aver * len(u)
#     print(upper * 2 + lower * 1, aver)      # 반례를 보면 문제점을 찾는데 도움이 되는데 제생각엔 이 코드 기준으로
# else:                                       # B=4 N=3 M=1 , 2칸이 1 한칸이 2 이면 ==> aver =3 , u 에 1개 ==> print(4,3) 이 나올텐데 print(4,4) 가 답일거고
#     print(upper * 2 + lower * 1, aver)      # B=2 N=10 M=10 , 1칸 100 나머지 1 ==> aver = 2, u 1개 upper은 97 lower 은 99 ==> print(98*2 +99, 2) 가 나올텐데
#                                             # print(99*2, 1) 이 답일 것 같습니다.

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
min_b = 257
max_b = -1
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if min(arr[i]) < min_b:
        min_b = min(arr[i])
    if max(arr[i]) > max_b:
        max_b = max(arr[i])

go = 0
height = 257
time = 500*500*2*256
for i in range(min_b, max_b + 1):
    go = i
    up = 0
    down = 0
    for j in range(N):
        for k in range(M):
            if arr[j][k] > go:
                down += arr[j][k] - go
            elif arr[j][k] < go:
                up += go - arr[j][k]
    if down - up + B < 0:
        continue
    else:
        result = down * 2 + up
        if result <= time:
            time = result
            height = i

print(time, height)

# down 은 갯수 * 2의 시간
# up은 갯수 * 1의 시간