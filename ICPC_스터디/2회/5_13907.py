N, M, K = map(int, input().split())
S, D = map(int, input().split())
# 도시수, 도로수, 세금인상횟수/ 출발도시, 도착도시/ 도시번호는 1부터
cost = dict()
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, f, c = map(int, input().split())
    cost[(s, f)] = c
    adj[s].append(f)
tax_up = []
for _ in range(K):
    tax_up.append(int(input()))

def search(s,f,cost=0,discovered=[]):
    discovered.append(s)
    for k in adj[s]:
        if not k in discovered:
            discovered = search(f, k ,discovered, 0)
    return discovered

def recursive_dfs(v, discovered=[]):
    discovered.append(v)  # discovered는 탐색한 노드들을 저장한다.
    for w in adj[v]:
        if not w in discovered:  # w가 탐색한 노드가 아니라면 탐색한다.
            discovered = recursive_dfs(w, discovered)
    return discovered