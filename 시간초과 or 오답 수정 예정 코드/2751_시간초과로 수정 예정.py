N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

for k in num:
    print(k)