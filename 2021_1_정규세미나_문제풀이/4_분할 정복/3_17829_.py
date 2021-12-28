# 입력
N = int(input())
for n in range(1,11):
    if 2 ** n == N:
        k = n
arr = []
for _ in range(N):
    temp = []
    for n in map(int, input().split()):
        temp.append(n)
    arr.append(temp)  # 2중 리스트


# 계산
def two(arr):  # arr = [[],[], .. ,[]] : n*n
    n = len(arr)
    m = n // 2
    for i in range(1, 11):
        if 2 ** i == n:
            k = i
    if k == 1:
        temp = arr[0] + arr[1]
        temp.sort()
        return temp[2]
    result = []
    for i in range(2):
        for j in range(2):
            temp = []
            for k in range(m):
                temp.append(arr[m*i+k][m*j:m*(j+1)])
            result.append(temp)
    return two(result)

print(two(arr))