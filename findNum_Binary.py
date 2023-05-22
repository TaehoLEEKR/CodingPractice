N = int(input())
Nlst = list(map(int,input().split()))
Nlst.sort()

M = int(input())
Mlst = list(map(int,input().split()))



for i in Mlst:
    left ,right  = 0 , len(Nlst)-1
    chk = False
    while left <= right :
        mid = (left + right) // 2
        if i == Nlst[mid]:
            print(1)
            chk = True
            break
        elif i < Nlst[mid]:
            right = right -1
        else:
            left = left +1
    if not chk :
        print(0)


            

        


