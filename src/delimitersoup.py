n = int(input())
s = input()

stack = []

def solve(s):
    for i, c in enumerate(s):
        if c in '({[':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return '%s %d'%(c, i)
            stack.pop()
        elif c == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return '%s %d'%(c, i)
            stack.pop()
        elif c == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return '%s %d'%(c, i)
            stack.pop()
    return 'ok so far'

print(solve(s))