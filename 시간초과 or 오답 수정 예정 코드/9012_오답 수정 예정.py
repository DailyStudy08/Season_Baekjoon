N = int(input())
lst = []
for i in range(N):
    a = input()
    lst += [a]
for st in lst:
    b = st.count('(')
    c = st.count(')')
    if b == c:
        if st[0] == '(':
            if st[-1] == ')':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')