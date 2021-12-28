N = int(input())
parent = list(map(int, input().split()))
tree = [[[], []] for _ in range(N)]  # [[parent], [child]]
for i in range(N):
    if parent[i] != -1:
        tree[i][0].append(parent[i])
        tree[parent[i]][1].append(i)

deleted = int(input())

print(tree)