import random

i = 0
lst = []
while i < 9:
    lst += [int(input())]
    i += 1

while True:
    a = random.sample(lst, 7)
    if sum(a) == 100:
        for n in sorted(a):
            print(n)
        break