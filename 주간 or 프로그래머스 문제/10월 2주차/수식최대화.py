def solution(expression):
    def check(cnt):
        nonlocal answer
        if cnt == 3:
            # print(cal_c)
            lst = num_lst[:]
            for i in range(2, -1, -1):
                idx = 0
                checdx = 0
                for j in range(3):
                    if cal_c[j] == i:
                        checdx = j
                        break
                while idx < len(lst):
                    if lst[idx] == cal[checdx]:
                        lst[idx - 1] = str(eval(lst[idx - 1] + lst[idx] + lst[idx + 1]))
                        lst.pop(idx)
                        lst.pop(idx)
                    else:
                        idx += 1

            if abs(int(lst[0])) > answer:
                answer = abs(int(lst[0]))
            return

        for i in range(3):
            if not visited[i]:
                visited[i] = 1
                cal_c[i] = cnt
                check(cnt + 1)
                visited[i] = 0
                cal_c[i] = None

    answer = 0
    n = ''
    cal = ['+', '-', '*']
    cal_c = [None] * 3
    num_lst = []
    for el in expression:
        if el in cal:
            num_lst.append(n)
            n = ''
            num_lst.append(el)
        else:
            n += el
    num_lst.append(n)

    visited = [0] * 3
    check(0)
    return answer


expression = input()
print(solution(expression))