N, L = map(int, input().split())
water = sorted([tuple(map(int, input().split())) for _ in range(N)])

covered, count = 0, 0
for i in range(N):
    start, end = water[i]
    start = max(start, covered)
    if (end - start) % L == 0:
        covered = end
        count += (end - start)//L
    else:
        covered = start + ((end - start)//L + 1) * L
        count += (end - start)//L + 1
print(count)