n = [input().split() for _ in range(int(input()))]
n.sort()
for i in n:
    print(*i)