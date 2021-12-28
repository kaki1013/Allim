from math import factorial


def combi(n, r):
    return factorial(n)//(factorial(n-r)*factorial(r))


M = int(input())
stone = sorted(list(map(int, input().split())))
N = sum(stone)
K = int(input())

bottom = combi(N, K)
top = 0
for i in range(M):
    if stone[i] >= K:
        top += combi(stone[i], K)

print(top/bottom)