N = 9
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

sum1 = [0]
sum2 = [0]
for i in range(2*N):
    if i % 2 == 0:
        sum1.append(sum1[-1] + arr1[i//2])
        sum2.append(sum2[-1])
    else:
        sum1.append(sum1[-1])
        sum2.append(sum2[-1] + arr2[(i-1) // 2])

YJ = False
for i in range(2*N+1):
    if sum1[i] > sum2[i]:
        YJ = True
        break

print("Yes" if YJ else "No")
