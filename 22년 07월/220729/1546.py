N = int(input())
a = list(map(int, input().split()))
b = sorted(a)
aver = b[-1]
average = []

for i in b:
    average += [i/b[-1]*100]
print(sum(average)/N)