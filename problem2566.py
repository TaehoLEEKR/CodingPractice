myList = [list(map(int, input().split())) for _ in range(9)]
maxList = []
for k,i in enumerate(myList,start=1):
    maxList.append([max(i),k,i.index(max(i))+1])

print(maxList)
result = max(maxList)
print(result[0])
print(result[1],result[2])