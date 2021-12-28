from collections import deque
import sys


def bfs(WorB, row, col):
    w, b = 0, 0
    if WorB == 'W':
        w += 1
    else:
        b += 1
    q = deque([(row, col)])
    visited[row][col] = True
    while q:
        now_r, now_c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt_r, nxt_c = now_r + dr, now_c + dc
            if 0 <= nxt_r < M and 0 <= nxt_c < N and not visited[nxt_r][nxt_c] and war[nxt_r][nxt_c] == WorB:
                q.append((now_r+dr, now_c+dc))
                visited[now_r+dr][now_c+dc] = True
                if WorB == 'W':
                    w += 1
                else:
                    b += 1
    return w**2, b**2


N, M = map(int, sys.stdin.readline().rstrip().split())
war = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

W, B = 0, 0
for row in range(M):
    for col in range(N):
        if not visited[row][col]:
            w, b = bfs(war[row][col], row, col)
            W += w
            B += b

print(W, B)
