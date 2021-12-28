def recursive_dfs(v, discovered=[]):
    discovered.append(v)  # discovered는 탐색한 노드들을 저장한다.
    for w in adj[v]:
        if not w in discovered:  # w가 탐색한 노드가 아니라면 탐색한다.
            discovered = recursive_dfs(w, discovered)
    return discovered



N, start, finish, M = map(int, input().split())
trans = dict()
for _ in range(M):
    s, f, cost = map(int, input().split())
    trans[(s,f)] = cost
# {(0, 1): 13, (1, 2): 17, (2, 4): 20, (0, 3): 22, (1, 3): 4747, (2, 0): 10, (3, 4): 10}
earn = list(map(int, input().split()))
# [0, 0, 0, 0, 0]
adj = [[] for _ in range(N)]
for t in trans.keys():
    a, b = t
    adj[a].append(b)
# [[1, 3], [2, 3], [4, 0], [4], []]

if not finish in recursive_dfs(start):
    print('gg')
if finish in recursive_dfs(start):
    pass