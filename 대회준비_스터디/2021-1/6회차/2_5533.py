N = int(input())
num_arr = [[] * N for _ in range(3)]
score = [0] * N

for _ in range(N):
    num = list(map(int, input().split()))
    for i in range(3):
        num_arr[i].append(num[i])
for i in range(3):
    num_arr[i].append(0)

for game in num_arr:
    for i in range(N):
        if game[i] not in game[:i] and game[i] not in game[i+1:]:
            score[i] += game[i]

for n in score:
    print(n)