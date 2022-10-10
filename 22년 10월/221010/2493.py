import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))
stack = []
for i in range(N):
    idx = len(stack) - 1
    while idx >= 0:
        if stack[idx][0] < lst[i]:
            stack.pop(idx)
        else:
            break
        idx -= 1
    print(stack[-1][1] + 1, end=' ') if stack else print(0, end=' ')
    stack.append((lst[i], i))
