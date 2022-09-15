import sys
input = sys.stdin.readline

N = int(input())
# 자식에게 부모 저장
arr = [0] * (N+1)
check = []
for _ in range(N-1):
    a, b = map(int, input().split())
    if a == 1:
        arr[b] = a
    elif b == 1:
        arr[a] = b
    else:
        if arr[a]:
            arr[b] = a
        elif arr[b]:
            arr[a] = b
        else:
            check.append([a, b])

print(check)
for i in range(2, N+1):
    print(arr[i])
