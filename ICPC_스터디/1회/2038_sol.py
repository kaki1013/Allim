# https://www.geeksforgeeks.org/golomb-sequence/
def Golomb(n):
    dp = [0] * (n + 1)

    # base cases
    dp[1] = 1
    # Finding and pring first
    # n terms of Golomb Sequence.
    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - dp[dp[i - 1]]]
    print(dp[n])


N = int(input())
Golomb(N)
