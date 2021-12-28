from sys import stdin
input = stdin.readline

N, M = map(int, input().strip().split())
No_eat = set([tuple(map(int, input().strip().split())) for _ in range(M)])

ans = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if (i, j) in No_eat or (j, i) in No_eat:
            continue
        for k in range(j+1, N+1):
            if (i, k) in No_eat or (k, i) in No_eat or (j, k) in No_eat or (k, j) in No_eat:
                continue
            ans += 1

print(ans)
