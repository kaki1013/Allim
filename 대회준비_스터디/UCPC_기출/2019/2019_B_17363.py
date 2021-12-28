N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

change = {'-': '|', '|': '-', '/': '\\', '\\': '/', '^': '<', '<': 'v', 'v': '>', '>': '^'}
ans = [['.' for _ in range(N)] for _ in range(M)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'O':
            ans[-1 - j][i] = 'O'
        if arr[i][j] not in {'.', 'O'}:
            ans[-1 - j][i] = change[arr[i][j]]

for line in ans:
    print(''.join(line))
