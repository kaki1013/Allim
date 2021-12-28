def second(n, arr):
    if n == 2:
        temp = []
        for i in range(2):
            for j in range(2):
                temp.append(arr[i][j])
        return sorted(temp)[-2]
    m = n // 2
    a1 = second(m, [arr[i][:m] for i in range(m)])
    a2 = second(m, [arr[i][m:] for i in range(m)])
    a3 = second(m, [arr[i][:m] for i in range(m, 2 * m)])
    a4 = second(m, [arr[i][m:] for i in range(m, 2 * m)])
    return second(2, [[a1, a2], [a3, a4]])


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(second(N, matrix))
