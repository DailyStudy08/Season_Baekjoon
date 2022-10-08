import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))
stack = []
for i in range(N):
    idx = 0
    for j in range(len(stack)):
        if stack[j] > lst[i]:
            idx = j + 1
    print(idx, end=' ')
    stack.append(lst[i])
