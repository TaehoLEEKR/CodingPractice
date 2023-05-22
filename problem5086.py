lst = []
while True:
    N,M =map(int,input().split())
    if N+M == 0:
        break
    if M % N == 0:
        lst.append("factor")
    elif N % M == 0:
        lst.append("multiple")
    else:
        lst.append("neither")

for i in lst:
    print(i)


