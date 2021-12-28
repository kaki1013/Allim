def golomb(n):
    sum_arr = [[1], [3], [5], [8], [11]] + [[0] for _ in range(44000)]  # sqrt2000000000 = 44721..
    if n == 1 or n == 2:
        return n
    k = 0
    while not sum_arr[k][0] < n <= sum_arr[k][0] + golomb(k + 2):
        k += 1
        sum_arr[k + 1][0] = sum_arr[k][0] + golomb(k + 2)
    return k + 2


N = int(input())
print(golomb(N))
