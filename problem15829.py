# import math
# length = int(input())
# strs = input()

# prime = 31
# mod = 1234567891

# has_res = 0

# for i in range(length):
#     chars = ord(strs[i]) - ord('a') +1 
#     has_res += (chars *(math.pow(prime,i)) % mod)

# has_res %= mod

# print(str(has_res)[:-2])
# 50점
n = int(input())
a = list(input())
result = 0
for i in range(n):
    result += ((ord(a[i])-96)*31**i)%1234567891
print(result%1234567891)