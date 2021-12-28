# 실패
import sys
from collections import deque
global cache, ski, lift


def bfs(S, T, K):
    queue = deque()
    cache[S] = 0
    queue.append([S, K])
    while len(queue) > 0:
        print(cache)
        point, k = queue.popleft()
        if not ((point > T) and (k == 0)):
            for i in ski[point]:
                nxt, t = i
                if cache[nxt] < cache[point] + t:
                    cache[nxt] = cache[point] + t
                    queue.append([nxt, k])
            if k > 0:
                for i in lift[point]:
                    if cache[i] < cache[point]:
                        cache[i] = cache[point]
                        queue.append([i, k - 1])


n, m, K, S, T = map(int, sys.stdin.readline().rstrip().split())

ski = [[] for _ in range(n + 1)]
lift = [[] for _ in range(n + 1)]
cache = [-1 for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    ski[a].append([b, t])
    lift[b].append(a)

bfs(S, T, K)

print(cache[T])
