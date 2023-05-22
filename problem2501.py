N,M = map(int,input().split())
lst = [i for i in range(1,N+1) if N % i == 0]
try:
    print(lst[M-1])
except:
    print(0)
