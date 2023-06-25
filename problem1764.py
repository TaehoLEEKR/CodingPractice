from collections import defaultdict
arr = []
n, m = map(int, input().split())
for i in range(n + m):
    arr.append(input())

nH = defaultdict(int)

lst = []
for i in arr:
    nH[i] += 1
for k,v in nH.items():
    if v >= 2:
        lst.append(k)
print(len(lst))
for i in sorted(lst):
    print(i)