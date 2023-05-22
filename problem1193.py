N = int(input())

count = 1 # 대각선

while N > count:
    N -= count
    count += 1

if count % 2 == 0:
    numer = N
    denomi = count - N + 1
else:
    numer =  count - N + 1
    denomi = N

print(f'{numer}/{denomi}')
