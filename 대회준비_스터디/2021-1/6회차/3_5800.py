K = int(input())

for i in range(1, K + 1):
    print(f'Class {i}')
    N, *arr = map(int, input().split())
    arr.sort()
    large_gap = arr[1] - arr[0]
    for j in range(N - 1):
        if arr[j+1] - arr[j] > large_gap:
            large_gap = arr[j+1] - arr[j]
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {large_gap}')