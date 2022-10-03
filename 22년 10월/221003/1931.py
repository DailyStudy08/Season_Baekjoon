N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))
arr = sorted(arr, key=lambda x: (x[1], x[0]))
cnt = 0
end = 0
for i in range(N):
    if arr[i][0] >= end:
        end = arr[i][1]
        cnt += 1
print(cnt)