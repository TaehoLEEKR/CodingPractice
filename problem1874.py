
# n = int(input())
# cnt = 1
# stack = []
# res = []
# for _ in range(n):
#     stackNum = int(input())
#     while cnt <= stackNum:
#         stack.append(cnt)
#         res.append('+')
#         cnt += 1
#     if stack[-1] == stackNum:
#         stack.pop()
#         res.append('-')
# print('\n'.join(map(str,res)))

n = [int(input()) for _ in range(int(input()))]
stack , res= [],[]
cnt = 1
for num in n:
    while cnt <= num:
        stack.append(cnt)
        res.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        print('NO')
        exit(0)
        
print('\n'.join(map(str,res)))