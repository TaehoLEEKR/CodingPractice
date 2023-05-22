import math
while True:
    n = list(map(int,input().split()))
    n.sort()
    if sum(n) == 0:
        break
    else:
        print('right' if math.pow(n[-1],2) == math.pow(n[0],2)+math.pow(n[1],2) else 'wrong')
