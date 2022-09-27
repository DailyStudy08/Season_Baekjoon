mo = ['a', 'e', 'i', 'o', 'u']


def check(lst, word, cnt, s, mo_cnt, za_cnt):
    if cnt == L:
        if mo_cnt and za_cnt >= 2:
            print(''.join(word))
    for i in range(s, C):
        word.append(lst[i])
        if lst[i] in mo:
            check(lst, word, cnt + 1, i + 1, mo_cnt + 1, za_cnt)
            word.pop()
        else:
            check(lst, word, cnt + 1, i + 1, mo_cnt, za_cnt + 1)
            word.pop()



L, C = map(int, input().split())
lst = sorted(input().split())
word = []
check(lst, word, 0, 0, 0, 0)
