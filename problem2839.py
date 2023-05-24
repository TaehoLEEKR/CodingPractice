N = int(input())
basket = 0
while N >= 5:
    if N % 5 == 0:
        basket += N // 5
        N = 0
        break
    N -= 3
    basket += 1
if N > 0:
    if N % 3 == 0:
        basket += N // 3
        N = 0
    else:
        print(-1)
        exit(0)
if N == 0:
    print(basket)
else:
    print(-1)
