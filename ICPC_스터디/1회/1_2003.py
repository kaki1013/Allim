# sol1: 시간 초과
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = 0

# for length in range(1, N+1):
#     for start in range(N-length+1):
#         if sum(arr[start:start+length]) == M:
#             ans += 1
# print(ans)

# sol2
N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]
for i in range(N):
    sum_arr.append(sum_arr[-1] + arr[i])

ans = 0
left, right = 0, 1
while (left, right) != (N, N):
    s = sum_arr[right] - sum_arr[left]
    if s == M:
        ans += 1
        left += 1
    elif s > M:
        left += 1
    elif s < M:
        if right < N:
            right += 1
        elif right == N:
            break

print(ans)
