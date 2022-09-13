import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
num = len(arr)
count = [0] * num
for i in range(1, num):
    count[i] = count[i-1] + arr[i]
# print(count)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(count[j] - count[i-1])