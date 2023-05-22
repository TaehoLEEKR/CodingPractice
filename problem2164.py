from collections import deque
deq = deque([i for i in range(1,int(input())+1)])

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    else:
        deq.popleft() # 첫 장 버리기
        card = deq.popleft() # 다음 장 
        deq.append(card) # 다음 장 맨 뒤로 옮기기
