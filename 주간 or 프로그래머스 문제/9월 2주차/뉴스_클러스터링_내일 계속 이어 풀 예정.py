def solution(str1, str2):
    str1.upper()
    str2.upper()
    answer = 0
    alpha = 'abcdefghijklnmopqrstuvwxyz'
    lst1 = []
    lst2 = []
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

    num1 = num2 = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                num1 += 1
                break
        else:
            num2 += 1
    return answer
