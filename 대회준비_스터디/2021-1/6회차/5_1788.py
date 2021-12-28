# 메모리 초과
n = int(input())
# n < 0 : f(n) = f(n+2) - f(n+1)
ans = 0

if n > 0:
    dp = [0, 1, 1] + [0] * 999998
    i = 0
    while dp[n] == 0:
        dp[i + 2] = (dp[i + 1] + dp[i]) % 1000000000
        i += 1
    ans = dp[n]
elif n < 0:
    dp = [1, -1] + [0] * 999998  # -1, -2, ...
    i = 0
    while dp[-n - 1] == 0:
        dp[i + 2] = dp[i] - dp[i + 1]
        i += 1
    ans = dp[-n - 1]

if n == 0:
    print(0)
elif ans > 0:
    print(1)
elif ans < 0:
    print(-1)

print(abs(ans) % 1000000000)

# 시간초과, 틀림
n = int(input())
# n < 0 : f(n) = f(n+2) - f(n+1)

ans = 0

if n > 0:
    ans_2 = 0
    ans_1 = 1
    ans = 1
    i = 1
    while i != n:
        temp = ans_1 + ans
        ans_2 = ans_1
        ans_1 = ans
        ans = temp
        i += 1
elif n < 0:
    ans_2 = 1
    ans_1 = -1
    ans = 2
    i = -1
    while i != n:
        temp = ans_1 - ans
        ans_2 = ans_1
        ans_1 = ans
        ans = temp
        i -= 1

if n == 0:
    print(0)
elif ans > 0:
    print(1)
elif ans < 0:
    print(-1)

print(abs(ans) % 1000000000)

# 아래 참고하여 수정
n = int(input())
ans = 0
positive = abs(n)
if positive != 0:
    dp = [0, 1]
    i = 0
    while len(dp) <= positive:
        dp.append((dp[i + 1] + dp[i]) % 1000000000)
        i += 1
    ans = dp[positive]

if n == 0:
    print(0)
elif n < 0 and n % 2 == 0:
    print(-1)
else:
    print(1)

print(ans)

# https://pacific-ocean.tistory.com/242
n = int(input())
s = [0, 1]
for i in range(2, abs(n) + 1):
    s.append((s[i - 1] + s[i - 2]) % 1000000000)
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(s[abs(n)])