# 시도횟수 N과 [[시도1, S, B], ...] 입력
N = int(input())
in_list = [list(map(int, input().split())) for _ in range(N)]
# 중복없고 0 없는 숫자 나열
case = list()
for i in range(100, 999):
    a, b, c = i // 100, (i // 10) % 10, i % 10
    if (a - b) * (b - c) * (c - a) != 0 and a * b * c != 0:
        case.append(100 * a + 10 * b + c)
# 답안용 리스트_조건에 안맞으면 제거함
ans = case[:]


# 비교값과 정답 입력시, [스트라이크, 볼] 출력하는 함수
def strike_ball(n, m):
    x, y = 0, 0
    for i in range(3):
        if str(n)[i] == str(m)[i]:
            x += 1
        if str(n)[i] != str(m)[i] and str(n)[i] in str(m):
            y += 1
    return [x, y]  # str, ball


# 각 스트라이크, 볼에 맞는 수만 남기고 제거
for n in range(N):
    for j in case:
        if strike_ball(in_list[n][0], j) != in_list[n][1:3] and j in ans:
            ans.remove(j)

print(len(ans))
