a, d, k = map(int, input().split())
p = d/100
q = k/100

n = 1
while p*(1+q)**(n-1) < 1:
    n += 1

# i번 승리시, 패배시 확률
win = [p]
lose = [1-p]
for _ in range(n-1):
    w = win[-1]
    win.append(w*(1+q))
    lose.append(1 - w*(1+q))
win[-1], lose[-1] = 1, 0

E = 0
for game in range(1, n+1):
    if game == 1:
        E += game * win[game-1]
        continue
    lose_p = 1
    for i in range(game-1):
        lose_p *= lose[i]
    E += game * lose_p * win[game-1]
E *= a

print(E)
