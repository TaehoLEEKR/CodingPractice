N,M = map(int , input().split())
nmList =[]
x,y = [],[]
for i in [x,y]:
    for j in range(N):
        i.append(list(map(int ,input().split())))

res = list(zip(x,y))
print(res)
for i,j in enumerate(res):
    nmList.append([j[0][i]+j[1][i] for i in range(N)])

for matrix in nmList:
    print(' '.join(map(str,matrix)))


