N = int(input())
ring = list(map(int, input().split()))
for i in range(1, N):
    a = ring[0]
    b = ring[i]
    j = ring[i]
    while j:
        if a % j == 0 and b % j == 0:
            a = a//j
            b = b//j
        j -= 1
    print(f'{a}/{b}')
