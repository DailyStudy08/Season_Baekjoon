from heapq import heappop, heappush
import sys
input = sys.stdin.readline

num_lst = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num:
        heappush(num_lst, -num)
    else:
        if num_lst:
            print(heappop(num_lst) * -1)
        else:
            print(0)