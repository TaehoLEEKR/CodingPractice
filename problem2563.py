num = int(input())
papers = [list(map(int, input().split())) for _ in range(num)]

board = [[0] * 100 for _ in range(100)]

for paper in papers:
    for i in range(paper[0], paper[0] + 10):
        for j in range(paper[1], paper[1] + 10):
            board[i][j] = 1

    area = 0
    for i in range(100):
        area += sum(board[i])

print(area)