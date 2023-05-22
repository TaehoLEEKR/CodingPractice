# import sys
# lst = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
# lst.sort()
# print('\n'.join(map(str,lst)))
import sys
num = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    temp = int(sys.stdin.readline())
    num[temp] += 1

for i in range(10001) :
    if num[i] != 0 :
        for j in range(num[i]) :
            print(i)
