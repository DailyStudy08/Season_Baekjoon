switch = int(input())
lights = [0]+ list(map(int, input().split()))
students = int(input())
for _ in range(students):
    s, sw_n = map(int, input().split())
    if s == 1:       # 남학생
        for i in range(1, switch + 1):
            if i % sw_n == 0:
                if lights[i] == 0:
                    lights[i] = 1
                else:
                    lights[i] = 0

    else:            # 여학생
        i = 0
        while 0 < sw_n-i and sw_n+i <= switch and lights[sw_n - i] == lights[sw_n + i]:
            if 0 < sw_n-i and sw_n+i <= switch and lights[sw_n - i] == lights[sw_n + i]:
                i += 1
        i -= 1
        for j in range(sw_n - i, sw_n + i + 1):
            if lights[j] == 0:
                lights[j] = 1
            else:
                lights[j] = 0
for l in range(1, switch+1):
    if l != 1:
        if (l-1) % 20 == 0:
            print()
    print(lights[l], end=' ')
