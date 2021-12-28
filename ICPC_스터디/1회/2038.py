def golomb(n):
    if n == 1 or n == 2:
        return n
    k = 1
    while not g_sum(k) < n <= g_sum(k + 1):
        k += 1
    return k + 1


def g_sum(i):
    golomb_sum = 0
    for num in range(1, i + 1):
        golomb_sum += golomb(num)
    return golomb_sum


N = int(input())
print(golomb(N))
