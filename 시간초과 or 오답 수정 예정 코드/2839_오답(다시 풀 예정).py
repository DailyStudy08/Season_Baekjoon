N = int(input())
s = 3
b = 5
result = 0
result += 3 * (N // 15)
b = N % 15

if b % 5 == 0:
    result += b // 5
elif b % 3 == 0:
    result += b // 3
elif b == 8:
    result += 2
elif b == 11:
    result += 3
elif b == 14:
    result += 4
elif b == 2 and N // 15 > 0:
    result += 2
else:
    result = result * 0 -1

print(result)

    