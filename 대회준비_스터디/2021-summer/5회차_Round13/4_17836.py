from collections import deque

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
time = 10**5

visited = [[False for _ in range(M)] for _ in range(N)]
q = deque([(0, 0, 0)])
while q:
    r, c, t = q.popleft()
    visited[r][c] = True

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nxt_r, nxt_c = r + dr, c + dc
        if 0 <= nxt_r < N and 0 <= nxt_c < M and not visited[nxt_r][nxt_c] and castle[nxt_r][nxt_c] in [0, 2]:
            if castle[nxt_r][nxt_c] == 2:
                time = min(time, (t + 1) + (N-1)-nxt_r + (M-1)-nxt_c)
            elif nxt_r == N-1 and nxt_c == M-1:
                time = min(time, t+1)
            else:
                q.append((nxt_r, nxt_c, t+1))
                visited[nxt_r][nxt_c] = True

print(time if time <= T else "Fail")
