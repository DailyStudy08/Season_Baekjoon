x,y,w,h = map(int, input().split())
a = []
a += [x-0, y-0, w-x, h-y]
b = sorted(a)
print(b[0])