arr = []
a, b = map(int, input().split())
arr.append(a/b)

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    arr.append(x/y)

print(min(arr)*1000)
