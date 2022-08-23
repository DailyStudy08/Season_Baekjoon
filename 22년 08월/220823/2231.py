N = int(input())
for i in range(N):
    result = i
    for j in str(i):
        result += int(j)
    if result == N:
        print(i)
        break
else:
    print(0)