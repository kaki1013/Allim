# sol1: 15650 조합 생성 참고 및 응용
N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

case = []
stack = [[0, []]]
while stack:
    now_idx, selected = stack.pop()
    if now_idx >= N:
        continue
    stack.append([now_idx + 1, selected])
    stack.append([now_idx + 1, selected+[ingredients[now_idx]]])
    if now_idx + 1 == N:
        case.append([now_idx + 1, selected])
        case.append([now_idx + 1, selected+[ingredients[now_idx]]])

min_diff = float('inf')
for i in range(2**N):
    now = case[i][1]
    if now:
        s, b = 1, 0
        for gred_s, gred_b in now:
            s *= gred_s
            b += gred_b
        if abs(s - b) < min_diff:
            min_diff = abs(s - b)
print(min_diff)

# sol2: 비트마스킹
N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
for case in range(1, 1 << N):
    s, b = 1, 0
    for element in range(N):
        if case & (1 << element):
            ingredient = ingredients[element]
            s *= ingredient[0]
            b += ingredient[1]
    min_diff = min(min_diff, abs(s - b))
print(min_diff)
