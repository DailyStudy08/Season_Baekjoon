N = int(input())
num = list(map(int, input().split()))

a = sorted(num)

print(a[0], a[-1])