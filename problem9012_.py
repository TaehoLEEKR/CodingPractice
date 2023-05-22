n = int(input())
i=0
while i < n:
    stack = list(input())
    res = []
    i+=1
    for k in stack:
        if k == '(':
            res.append(k)
        elif k == ')':
            try:
                res.pop()
            except:
                res.append(k)
                break
    if len(res) == 0:
        print('YES')
    else:
        print('NO')
            
    

