def solution(n, t, m, p):
    num_dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    answer = ''
    numlst = [0]
    for i in range(1, t*m):
        temp_n = []
        while i:
            temp_n.append(num_dic[i % n])
            i //= n
        for j in range(len(temp_n)-1, -1, -1):
            numlst.append(temp_n[j])
        if len(numlst) > t*m:
            break
    for i in range(len(numlst)):
        if i % m == p - 1:
            answer += str(numlst[i])
        if len(answer) == t:
            break
    return answer

n, t, m, p = map(int, input().split())
print(solution(n, t, m, p))
