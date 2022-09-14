N = int(input())
num = int(N**(0.5))
cnt = 0
for i in range(num+1, 0, -1):
    while i*i <= N:
        N -= i*i
        cnt += 1
print(cnt)