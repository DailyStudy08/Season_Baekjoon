S = input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    for j in range(len(S)):
        if S[j] == i:
            print(j, end=' ')
            break
    else:
        print(-1, end=' ')