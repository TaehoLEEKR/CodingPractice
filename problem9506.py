result =[]
strs = ""
while True:
    N = int(input())
    if N == -1: 
        break
    lst = [i for i in range(1,N+1) if N % i == 0]
    if sum(lst[:-1:]) == lst[-1]:
        strs = f'{lst[-1]} = {" + ".join(map(str,lst[:-1:]))}'
        result.append(strs)
    else:
        strs =f'{lst[-1]} is NOT perfect.'
        result.append(strs)
for i in result:
    print(i)
