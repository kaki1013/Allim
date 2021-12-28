x = list(input())
num = 0
while not x + x[:num][::-1] == x[:num] + x[::-1]:
    num += 1

print(num+len(x))
