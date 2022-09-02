import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = {}
for _ in range(16):
    a, b = sys.stdin.readline().rstrip().split()
    arr[a] = b
for _ in range(M):
    c = sys.stdin.readline().rstrip()
    print(arr[c],end='\n')