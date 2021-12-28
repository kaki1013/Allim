"""
1. 사이클 찾기
DFS를 통해서 그래프 순회 & DFS 스택 내에 있는 경로를 다시 방문하려 한다면 그 부분이 사이클
알림 2020년 1학기 정기스터디 5주차
주소
https://www.acmicpc.net/group/board/view/533/17329  // 영상 46:22 참고

2. 문제 풀이
정점과 간선이 모두 N개 존재하고 임의의 두 정점 사이에 경로가 존재하므로 사이클은 1개만 존재한다
사이클을 이루는 정점은 거리가 0이고, 이외의 정점들은 거리가 1 이상이다

 1 ----
 2    |
 3 --|
| \
4 5
6
"""
from collections import deque
import sys
sys.setrecursionlimit(5000)


def DFS(graph, stack, inStack, now, parent):  # 트리에 간선이 하나 추가된 형태이므로 visited 배열이 불필요 & 사이클이 반드시 하나 존재
    if inStack[now]:
        return

    stack.append(now)
    inStack[now] = True
    for dest in graph[now]:
        if dest != parent:
            if inStack[dest]:
                for i in range(len(stack)):
                    if dest == stack[i]:
                        global cycle
                        cycle = stack[i:]
                        return
            DFS(graph, stack, inStack, dest, now)
    stack.pop()
    inStack[now] = False
    return


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

inStack = [False] * N
stack = []
DFS(graph, stack, inStack, 0, -1)
cycle = set(cycle)

dist = [0] * N
for i in range(N):
    visited = [False] * N
    if i not in cycle:
        q = deque([(i, 0)])
        while q:
            now, distance = q.popleft()
            visited[now] = True
            if now in cycle:
                dist[i] = distance
                break
            for nxt in graph[now]:
                if not visited[nxt]:
                    q.append((nxt, distance+1))
print(*dist)

"""
출처: https://www.acmicpc.net/source/11868926
__import__('sys').setrecursionlimit(923123)
input = __import__('sys').stdin.readline
from collections import deque


def dfs(v, dep):
    depth[v] = dep
    for u in adj[v]:
        if depth[u]:
            if depth[u] == dep - 1:
                continue
            Q.append(v)
            return depth[u]
        d = dfs(u, dep+1)
        if 0 < d <= depth[v]:
            Q.append(v)
            return d
    return -1


n = int(input())
adj = [[] for i in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
depth = [0]*(n+1)
Q = deque()
dfs(1, 1)

dist = [-1]*(n+1)
for v in Q:
    dist[v] = 0
while Q:
    p = Q.popleft()
    for q in adj[p]:
        if dist[q] != -1:
            continue
        dist[q] = dist[p]+1
        Q.append(q)
print(*dist[1:])
"""