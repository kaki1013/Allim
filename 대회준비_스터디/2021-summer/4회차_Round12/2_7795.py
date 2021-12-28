T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = sorted(list(map(int, input().split())))

    ans = 0
    if B == 1:
        for a in arr1:
            if a > arr2[0]:
                ans += 1
    elif B == 2:
        for a in arr1:
            if a <= arr2[0]:
                continue
            else:
                ans += 1
                if a > arr2[1]:
                    ans += 1
    else:
        for a in arr1:
            left, right = 0, B-1
            if a <= arr2[left]:
                continue
            elif a > arr2[right]:
                ans += B
                continue
            while right - left > 1:
                m = (left + right) // 2
                if a > arr2[m]:
                    left = m
                elif a <= arr2[m]:
                    right = m
            ans += right
    print(ans)
