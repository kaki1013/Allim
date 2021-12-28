def g_sum(i):
    if arr[i] != 0:
        return arr[i]
    arr[i] = arr[i-1] + golomb(i)
    return arr[i]


def golomb(n):
    if n == 1 or n == 2:
        return n
    k = 1
    while not g_sum(k) < n <= g_sum(k + 1):
        k += 1
    return k + 1


arr = [0]*673366
arr[1] = 1

N = int(input())
print(golomb(N))