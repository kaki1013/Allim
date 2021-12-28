import sys
from collections import deque
global n, m, before, after
dir_row = [-1, 0, 1, 0]
dir_col = [0, 1, 0, -1]


def find():
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if before[row][col] != after[row][col]:
                return row, col
    return row, col


def inject(row, col):
    exnum = before[row][col]
    newnum = after[row][col]
    if exnum == newnum:
        return
    queue = deque()
    before[row][col] = newnum
    queue.append([row, col])
    while len(queue) > 0:
        r, c = queue.popleft()
        for i in range(4):
            if before[r + dir_row[i]][c + dir_col[i]] == exnum:
                before[r + dir_row[i]][c + dir_col[i]] = newnum
                queue.append([r + dir_row[i], c + dir_col[i]])


n, m = map(int, sys.stdin.readline().rstrip().split())
before = [[0 for _ in range(m + 2)]]
after = [[0 for _ in range(m + 2)]]
for _ in range(n):
    before.append([0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0])
before.append([0 for _ in range(m + 2)])
for _ in range(n):
    after.append([0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0])
after.append([0 for _ in range(m + 2)])
row, col = find()

inject(row, col)

row, col = find()
if (row == n) and (col == m) and (before[row][col] == after[row][col]):
    print("YES")
else:
    print("NO")