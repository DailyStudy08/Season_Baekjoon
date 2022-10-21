visited = []
answer = 0


def nqeen(n):
    global answer
    if len(visited) == n:
        answer += 1
        return
    for i in range(n):
        if i not in visited:
            cnt = 0
            for j in range(len(visited)):
                if abs(visited[j] - i) != abs(len(visited) - j):
                    cnt += 1

            if cnt == len(visited):
                visited.append(i)
                nqeen(n)
                visited.pop()


nqeen(int(input()))
print(answer)