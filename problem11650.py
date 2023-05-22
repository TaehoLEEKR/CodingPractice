import sys
res = []
for i in range(int(input())):
    res.append(list(map(int,input().split())))
result = sorted(res)
for i in result:
    print(*i)