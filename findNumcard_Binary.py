N = int(input())
Nlst = sorted(list(map(int,input().split())))


M = int (input())
Mlst = list(map(int,input().split()))

res = []
for i in Mlst:
    left = 0
    right = N-1
    chk = False
    while (left <= right):
        mid = left + (right - left) // 2

        if i  == Nlst[mid]:
            res.append(1)
            chk = True
            break
        elif i < Nlst[mid]:
            right = mid -1
        else:
            left = mid + 1
    if not chk:
        res.append(0)
print(' '.join(map(str,res)))
