import sys

n = int(input())
num = sorted([int(sys.stdin.readline()) for _ in range(n)])
print('\n'.join(map(str,num)))