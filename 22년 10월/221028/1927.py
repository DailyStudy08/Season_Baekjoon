from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(heap, x)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)