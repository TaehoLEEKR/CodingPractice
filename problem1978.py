# n=int(input())
# a = [False,False] + [True]*(n-1)
# primes=[]

# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(primes)


def isPrime(num):
    return [False for i in range(2,num) if num % i == 0 ]
    


N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
# lst = [int(input().split(' ')) for _ in range(N)]
cnt = 0

for i in lst:
    if i == 1:
        continue
    elif isPrime(i) == []:
        cnt +=1
print(cnt)





