while True:
    a = input()
    if a == '.':
        break
    stack = []
    result = 'yes'
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break
    if stack:
        result = 'no'
    print(result)