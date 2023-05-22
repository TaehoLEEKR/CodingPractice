import sys

N = int(sys.stdin.readline().strip())
Nlst = []
#sorted(list(map(int,sys.stdin.readline().strip().split())))

for i in range(0,N):
    Nlst.append(sys.stdin.readline().strip())
for i in sorted(Nlst):
    print(i)

