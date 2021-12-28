K = int(input())
city = [0] * 2 ** K
order = [0] + list(map(int, input().split()))
visited = {0}

now = 2 ** (K - 1)
i = 1
while len(visited) != 2 ** K:
    if 2 * now <= 2 ** K - 1 and 2 * now not in visited:
        now = 2 * now
    elif now <= 2 ** K - 1 and now not in visited:
        city[now] = order[i]
        visited.add(now)
        i += 1
    elif 2 * now + 1 <= 2 ** K - 1 and 2 * now + 1 not in visited:
        now = 2 * now + 1
    else:
        now = now // 2

for i in range(K):
    print(*city[2**i:2**(i+1)])
