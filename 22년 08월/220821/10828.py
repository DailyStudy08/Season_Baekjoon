import sys

def push(num):
    stack.append(num)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

def size():
    print(len(stack))

def s_pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def empty():
    if stack:
        print(0)
    else:
        print(1)

stack = []
N = int(sys.stdin.readline())
for _ in range(N):
    go = sys.stdin.readline().split()
    if go[0] == 'push':
        push(go[1])
    elif go[0] == 'top':
        top()
    elif go[0] == 'size':
        size()
    elif go[0] == 'empty':
        empty()
    elif go[0] == 'pop':
        s_pop()