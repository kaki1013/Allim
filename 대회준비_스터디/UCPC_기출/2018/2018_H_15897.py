# 참고: https://js1jj2sk3.tistory.com/109
N = int(input()) - 1
div = [0]
for i in range(1, int(N**0.5) + 1):
    if i == N // i:
        div.append(i)
    else:
        div.append(i)
        div.append(N // i)
div.sort()

ans = N + 1
l = len(div)
for i in range(1, l):
    ans += div[i] * (div[l - i] - div[l - i - 1])

print(ans)

# https://www.acmicpc.net/source/14530791
N = int(input())
sqrtN = int(((N - 1) ** 0.5))

res = 0
for i in range(1, sqrtN+1):
    res += (N-1) // i

print(N - sqrtN*sqrtN + res*2)