def binggogame(arr, num):
    binggo = [0] * 12
    result = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if arr[k][l] == num[i][j]:
                        binggo[k] += 1
                        binggo[l + 5] += 1
                        if k + l == 4:
                            binggo[10] += 1
                        if k == l:
                            binggo[11] += 1
                        break
                cnt = 0
                for n in range(12):
                    if binggo[n] == 5:
                        cnt += 1
                        if cnt >= 3:
                            result = i * 5 + j + 1
                            return result



arr = [list(map(int, input().split())) for _ in range(5)]

# 가로 0 1 2 3 4 세로 0 1 2 3 4 대각선 1 2 
num = [list(map(int, input().split())) for _ in range(5)]


print(binggogame(arr, num))