# import sys
# def reqursive_count(floor, room):
#     if room == 1:  
#         return 1
#     elif floor == 0:  
#         return room
#     else:
#         return  reqursive_count(floor - 1, room) +  reqursive_count(floor, room - 1)

# n = int(sys.stdin.readline())  

# for _ in range(n):
#     k = int(sys.stdin.readline())  
#     n = int(sys.stdin.readline())  
#     result =  reqursive_count(k, n)
#     print(result)

n = int(input())  

for _ in range(n):
    k = int(input()) 
    n = int(input()) 

    
    people = [x for x in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]  

    result = people[-1]  
    print(result)
