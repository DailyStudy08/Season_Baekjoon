T = int(input())
for tc in range(T):
    a, b = input().split()
    for r in b:
        print(r*int(a), end = '')
    print()