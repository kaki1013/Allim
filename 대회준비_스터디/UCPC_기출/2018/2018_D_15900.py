# 각 리프노드에서 루트노드까지의 거리의 총합(= 게임의 진행 횟수)이 홀수인가 짝수인가
# pypy3로 통과
from collections import deque
import sys


def bfs(adj, start, visited, dist):
    q = deque([start])
    visited[start] = True
    dist[start] = 0

    while q:
        now = q.popleft()
        for nxt in adj[now]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                dist[nxt] = dist[now] + 1
    return dist


N = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child = map(int, sys.stdin.readline().rstrip().split())
    adj[parent].append(child)
    adj[child].append(parent)
distance = bfs(adj, 1, [False] * (N + 1), [0] * (N + 1))
leaves = [i for i in range(2, N + 1) if len(adj[i]) == 1]

count = 0
for leaf in leaves:
    count += distance[leaf]

print('Yes' if count % 2 == 1 else 'No')

# https://www.acmicpc.net/source/21642531
# python3 통과 코드
import sys


def backtracking(node, cnt):
    global total_cnt
    visited[node] = True
    is_leaf = True
    for child in tree[node]:
        if not visited[child]:
            backtracking(child, cnt+1)
            is_leaf = False
    if is_leaf:
        total_cnt += cnt


read = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(read())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, read().split())
    tree[a].append(b)
    tree[b].append(a)

total_cnt = 0
visited = [False] * (n+1)

backtracking(1, 0)
print('Yes' if total_cnt % 2 == 1 else 'No')
