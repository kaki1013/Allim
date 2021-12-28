# 1. 같은 행 또는 열은 2번 이상 뒤집지 않음
# 2. T > H 일 때는 뒤집는 게 이득
# 특히 2. 에 의해 행(또는 열)만을 뒤집는 경우들을 살펴보면, 즉 2^20=10^6의 경우를 살펴보면 충분
# 각 경우들에 대해서 어떤 열(또는 행)을 뒤집을지는 2에 의해서 결정이 가능하기 때문
N = int(input())
coins = [list(input()) for _ in range(N)]

min_tail = 0
for coin in coins:
    for c in coin:
        if c == 'T':
            min_tail += 1

for case in range(1 << N):  # 행의 상태를 결정
    tail = 0  # 각 상태에 대한 tail 개수 체크 -> 기존까지의 최소 뒷면 개수보다 작으면 업데이트
    for col in range(N):  # 각 열을 훑어봄
        h, t = 0, 0  # 해당 열에 대한 앞면과 뒷면의 개수를 카운트
        for row in range(N):  # 몇번째 행을 살펴보는지 / 각 행이 뒤집어졌는지 체크 의 2가지 역할
            mask = 1 << row
            if case & mask:  # 이 행을 뒤집는다면, H: t += 1 & T: h += 1
                if coins[row][col] == 'H':
                    t += 1
                else:
                    h += 1
            else:  # 이 행을 뒤집지 않는다면, H: h += 1 & T: t += 1
                if coins[row][col] == 'H':
                    h += 1
                else:
                    t += 1
        tail += min(h, t)  # 열을 뒤집으면서 T의 개수가 최소가 되도록 함
    # 각 행의 상태에 따른 열의 상태를 결정한 상태에서 얻은 최소 뒷면 개수와 기존의 값을 비교하여 업데이트
    min_tail = min(min_tail, tail)

print(min_tail)
