n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if arr[r][c] == 0:
        arr[r][c] = 2

    for _ in range(4):
        nd = (d + 3) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]

        if arr[nx][ny] == 0:
            r, c, d = nx, ny, nd
            break
        d = nd

    else:
        bd = (d + 2) % 4
        br = r + dx[bd]
        bc = c + dy[bd]

        if arr[br][bc] == 1:
            break


        r,c = br, bc
count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            count += 1

print(count)
