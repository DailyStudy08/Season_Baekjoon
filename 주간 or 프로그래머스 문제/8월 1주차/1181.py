N = int(input())
word = []
for i in range(N):
    word += [input()]
w_l = list(set(word))
dic = sorted(w_l, key = lambda x : (len(x), x))
for w in dic:
    print(w)