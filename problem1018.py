n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_diff(board, start_color):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and board[i][j] != start_color:
                cnt += 1
            elif (i+j) % 2 == 1 and board[i][j] == start_color:
                cnt += 1
    return cnt

min_diff = n * m
for i in range(n-7):
    for j in range(m-7):
        cnt1 = count_diff([row[j:j+8] for row in board[i:i+8]], 'W')
        cnt2 = count_diff([row[j:j+8] for row in board[i:i+8]], 'B')
        min_diff = min(min_diff, cnt1, cnt2)

print(min_diff)
