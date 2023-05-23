import sys
res = []
for i in range(int(input())):
    x,y = map(int,input().split())
    res.append((x,y))

print(res)

result = sorted(res,key=lambda x : x[1])
for i in result:
    print(i[0],i[1])

