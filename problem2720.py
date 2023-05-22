# 124 - > 4(0.25 * 4) 2(0.1 *2 ) 0(0.05 * 0) 4(0.01 *4)

N = int(input())
res = []
for i in range(N):
    money = int(input())
    qt = money // 25 # 0.25 센트
    money %= 25  # 잔돈
    di = money // 10 # 0.1
    money %= 10 # 잔돈
    nic = money // 5  # 0.5
    money %= 5
    pen = money
    res.append([qt,di,nic,pen])

for i in res:
    print(*i)





