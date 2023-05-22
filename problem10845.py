from collections import deque
import sys


def push(lst , number):
    lst.append(number)
    return lst

def pop(lst): 
    if empty(lst) == 1:
        return -1
    popData = lst.popleft()
    return popData

def size(lst): return len(lst)
def empty(lst): return 1 if len(lst) == 0 else 0


deq = deque()
input = sys.stdin.readline
printLst = []

for _ in range(int(input())):
    que = list(input().split())
    cmd = que[0]
    if cmd == 'push':
        push(deq,que[1])
    elif cmd =='front':
        printLst.append((deq[0] if len(deq) != 0 else -1))
    elif cmd == 'back':
        printLst.append(deq[-1] if len(deq) != 0 else -1)
    elif cmd == 'size':
        printLst.append(size(deq))
    elif cmd == 'empty':
        printLst.append(empty(deq))
    elif cmd == 'pop':
        printLst.append(pop(deq))
print('\n'.join(map(str,printLst)))