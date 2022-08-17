# ############### 오답
# N = int(input())
# lst = []
# for i in range(N):
#     a = input()
#     lst += [a]
# for st in lst:
#     b = st.count('(')
#     c = st.count(')')                       # 개수가 동일 한것 외에도 체크가 필요할 것 같습니다.
#     if b == c:
#         if st[0] == '(':
#             if st[-1] == ')':               
#                 print('YES')                # 반례로 '() )( ()' 가 있을 것 같네요.
#             else:
#                 print('NO')
#         else:
#             print('NO')
#     else:
#         print('NO')

################# 스택 배운 후 다시 풀어보기

N = int(input())
for i in range(N):
    arr = list(input())
    lst = []
    a = ''
    for el in arr:
        if el == '(':
            lst.append(el)
        else:
            try:
                a = lst.pop(-1)
            except:
                a = 'NO'
                break
    if a == 'NO':
        print(a)
    else:
        if len(lst) == 0:
            print('YES')
        else:
            print('NO')
