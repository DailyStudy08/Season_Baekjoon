import sys

def add(num):
    S.add(num)


def check(num):
    if num in S:
        print(1)
    else:
        print(0)


def remove(num):
    if num in S:
        S.remove(num)


def toggle(num):
    if num in S:
        S.remove(num)
    else:
        S.add(num)


N = int(sys.stdin.readline())
S = set()
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'add':
        add(int(a[1]))
    elif a[0] == 'check':
        check(int(a[1]))
    elif a[0] == 'remove':
        remove(int(a[1]))
    elif a[0] == 'toggle':
        toggle(int(a[1]))
    elif a[0] == 'all':
        S.update(x for x in range(1, 21))
    elif a[0] == 'empty':
        S.clear()
