from collections import deque

n,m = map(int,input().split())
deq = deque(i for i in range(1,n+1))
res = []
cnt = 0

while len(deq) != 0:
    popData = deq.popleft()
    cnt += 1

    if cnt % m == 0:
        res.append(popData)
    else:
        deq.append(popData)
print('<'+', '.join(map(str,res)) + '>')



