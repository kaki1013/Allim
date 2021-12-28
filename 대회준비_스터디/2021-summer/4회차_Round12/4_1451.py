# 추가: https://suri78.tistory.com/151  //  이중 리스트 내포를 통해서 코드 간략화 가능
N, M = map(int, input().split())
rect = [list(map(int, list(input()))) for _ in range(N)]

# dp[r][c] := (1, 1)과 (r, c)를 각각 좌상부와 우하부의 꼭지점으로 가지는 정사각형 내의 꼭지점의
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for row in range(1, N+1):
    for col in range(1, M+1):
        dp[row][col] = dp[row][col-1] + dp[row-1][col] - dp[row-1][col-1] + rect[row-1][col-1]

ans = -1
for a in range(1, M-1):
    for b in range(a+1, M):
        rect1 = dp[N][a]
        rect2 = dp[N][b] - dp[N][a]
        rect3 = dp[N][M] - dp[N][b]
        ans = max(ans, rect1 * rect2 * rect3)

for a in range(1, N-1):
    for b in range(a+1, N):
        rect1 = dp[a][M]
        rect2 = dp[b][M] - dp[a][M]
        rect3 = dp[N][M] - dp[b][M]
        ans = max(ans, rect1 * rect2 * rect3)

for a in range(1, N):
    for b in range(1, M):
        rect1 = dp[a][b]
        rect2 = dp[a][M] - dp[a][b]
        rect3 = dp[N][M] - dp[a][M]
        rect4 = dp[N][b] - dp[a][b]
        rect5 = dp[N][M] - dp[N][b]
        ans = max(ans, rect1 * rect2 * rect3, rect1 * rect4 * rect5)

for a in range(2, N+1):
    for b in range(2, M+1):
        rect1 = dp[N][M] - dp[a-1][M] - dp[N][b-1] + dp[a-1][b-1]
        rect2 = dp[a-1][M]
        rect3 = dp[N][b-1] - dp[a-1][b-1]
        rect4 = dp[N][b-1]
        rect5 = dp[a-1][M] - dp[a-1][b-1]
        ans = max(ans, rect1 * rect2 * rect3, rect1 * rect4 * rect5)

print(ans)
