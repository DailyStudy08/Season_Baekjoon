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
    
    # 버블 sort 하면 시간초과 날거여..
    # 그냥 sort 함수 쓰거나 그게 싫은거면 quick sort , merge sort를 구현할 수 있게 공부해야하도록..
