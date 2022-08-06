word = input().lower()
w_s = list(set(word))
c = []
for i in w_s:
    c += [word.count(i)]

a = sorted(c)
if len(a) == 1:
    print(word.upper())
elif a[-1] == a[-2]:
    print('?')
else:
    print(w_s[(c.index(a[-1]))].upper())
