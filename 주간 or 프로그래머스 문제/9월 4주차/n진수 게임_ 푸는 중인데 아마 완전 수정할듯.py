def solution(n, t, m, p):
    answer = ''
    dict_num = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    num = 0
    t_list = []                                                     # t가 말해야하는 숫자를 넣는 리스트
    while len(t_list) < t:
        if num > 0 and num % t == p - 1:
            t_n = ''
            num = str(num)
            for i in range(len(num)):
                t_n +=
            t_list.append(t_n)
    return answer


n, t, m, p = map(int, input().split())
print(solution(n, t, m, p))
