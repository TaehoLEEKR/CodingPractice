import sys

def is_stack(strs):
    stack = []

    for char in strs:
        if char == '(' or char == '[':
            stack.append(char)
        elif char ==')' or char == ']':
            if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return not stack



while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    if is_stack(line):
        print('yes')
    else:
        print('no')