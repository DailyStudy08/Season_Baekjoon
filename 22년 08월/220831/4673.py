def d(n):
    for i in str(n):
        n += int(i)
    return n

memo = []
for i in range(1, 10001):
    memo.append(d(i))

# print(memo)

for i in range(1, 10001):
    if i in memo:
        pass
    else:
        print(i)