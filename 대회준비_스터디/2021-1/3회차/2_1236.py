N, M = map(int, input().split())  # 행, 열
board = [list(input()) for _ in range(N)]

row_people, column_people = set(), set()
for row in range(N):
    for column in range(M):
        if board[row][column] == 'X':
            row_people.add(row)
            column_people.add(column)

print(max(N-len(row_people), M-len(column_people)))
