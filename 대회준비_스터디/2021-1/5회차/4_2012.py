# 그리디 정당화: https://blog.encrypted.gg/308
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

bul_man = 0
for i in range(N):
    bul_man += abs(arr[i]-(i+1))
print(bul_man)