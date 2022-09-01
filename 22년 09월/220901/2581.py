M = int(input())
N = int(input())
answer = []
for i in range(M, N+1):
    result = []
    for j in range(1, i+1):
        if i % j == 0:
            result.append(j)
    if len(result) == 2:
        answer.append(i)

if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)