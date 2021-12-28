a = [int(input()) for _ in range(9)]
s = sum(a)

for i in range(9):
    check = s - 100 - a[i]
    if check in a and a[i] != check:
        a.remove(a[i])
        a.remove(check)
        for j in a:
            print(j)
        break