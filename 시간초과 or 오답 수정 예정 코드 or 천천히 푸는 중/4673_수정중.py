def d(n):
    for i in str(n):
        n += int(i)
    return n

def selfnumber(n):
    for i in range(n):
        if d(i) == n:
            return None
    return n

for i in range(1, 10001):
    a = selfnumber(i)
    if a:
        print(a)


#### memoization 할 수 있을 거 같은데 내일 마저 시도해보겠습니다.