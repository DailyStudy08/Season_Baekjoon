i = 0
a = []
while i < 9:
    a += [int(input())]
    i += 1
b = sorted(a)
print(b[-1])
print(a.index(b[-1])+1)