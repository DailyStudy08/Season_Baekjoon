def findnum(n):
    num = None
    temp = 10000
    for i in range(4):
        check = n[i % 4] + n[(i + 1) % 4] + n[(i + 2) % 4] + n[(i + 3) % 4]
        if int(check) < temp:
            temp = int(check)
            num = temp
    return num


number = (''.join(input().split()))
num = findnum(number)
result = 0
c = 1111
visitied = []

while num != c:
    check_num = findnum(str(c))
    if '0' not in str(c) and check_num not in visitied and check_num < num:
        visitied.append(check_num)
        result += 1
    c += 1
print(result + 1)
