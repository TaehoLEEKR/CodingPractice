from collections import defaultdict

n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n-1):
    b.append(input())

nH = defaultdict(int)

for name in a:
    nH[name] +=1
for name in b:
    nH[name] -=1
