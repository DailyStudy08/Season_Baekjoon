def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    answer = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lst1 = []
    lst2 = []
    check2 = []
    for i in range(1, len(str1)):
        a = str1[i-1] + str1[i]
        for j in a:
            if j not in alpha:
                break
        else:
            lst1.append(a)

    for i in range(1, len(str2)):
        a = str2[i-1] + str2[i]
        for j in a:
            if j not in alpha:
                break
        else:
            lst2.append(a)
            check2.append(a)

    num1 = 0
    for i in range(len(lst1)):
        for j in range(len(check2)):
            if lst1[i] == check2[j]:
                num1 += 1
                check2[j] = None
                break

    num2 = len(lst1) + len(lst2) - num1
    if num2 == 0:
        result = 1
    else:
        result = num1/num2
    answer = int(result * 65536)
    return answer
