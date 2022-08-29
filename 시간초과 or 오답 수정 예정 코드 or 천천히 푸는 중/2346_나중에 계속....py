N = int(input())
arr = [0] + list(map(int, input().split()))
ball = [0] * (N+1)
a = 1
idx = 0
while 0 in ball:
    idx += a
    ball[idx] = 1
    print(idx)
    a = arr.pop(a)