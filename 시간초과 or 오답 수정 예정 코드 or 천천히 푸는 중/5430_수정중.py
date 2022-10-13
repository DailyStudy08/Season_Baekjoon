import sys
# input = sys.stdin.readline


def check():
    global num_lst
    global s
    global e

    for fx in p:
        if fx == 'R':
            if s != 0:
                pass
            else:

        elif fx == 'D':
            if num_lst:
                num_lst.pop(0)
            else:
                return 0
    return 1


T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    num_f = input().lstrip('[').rstrip(']').split(',')
    print(num_f)
    if num_f != ['']:
        num_lst = list(map(int, num_f))
    else:
        num_lst = []
    result = 0
    s = 0
    e = len(num_lst)
    if check():
        print('[', end='')
        for num in range(len(num_lst)-1):
            print(num_lst[num], end=',')
        print(f'{num_lst[-1]}]')
    else:
        print('error')
