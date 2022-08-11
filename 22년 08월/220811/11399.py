N = int(input())
time = sorted(list(map(int, input().split())))
for i in range(1, N):
    time[i] += time[i-1]
print(sum(time))
