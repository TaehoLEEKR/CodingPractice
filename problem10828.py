import sys
def push(lst , number):
    lst.append(number)
    return lst

def pop(lst): 
    if empty(lst) == 1:
        return -1
    popData = lst.pop()
    return popData

def size(lst): return len(lst)
def empty(lst): return 1 if len(lst) == 0 else 0
def top(lst): return lst[-1] if empty(lst) == 0 else -1

res = list()
input = sys.stdin.readline
printLst = []
for _ in range(int(input())):
    stack = list(input().split())
    cmd = stack[0]
    if cmd == 'push':
        push(res,stack[1])
    elif cmd == 'top':
        printLst.append(top(res))
    elif cmd == 'size':
        printLst.append(size(res))
    elif cmd == 'empty':
        printLst.append(empty(res))
    elif cmd == 'pop':
        printLst.append(pop(res))
print('\n'.join(map(str,printLst)))
