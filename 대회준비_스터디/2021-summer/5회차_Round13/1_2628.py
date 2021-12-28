x, y = map(int, input().split())
x_cut, y_cut = [0], [0]
n = int(input())
for _ in range(n):
    cmd, where = map(int, input().split())
    if cmd == 1:
        x_cut.append(where)
    else:
        y_cut.append(where)
x_cut.append(x)
y_cut.append(y)
x_cut.sort()
y_cut.sort()
lx, ly = len(x_cut), len(y_cut)

x_length = []
y_length = []
for i in range(lx-1):
    x_length.append(x_cut[i+1]-x_cut[i])
for i in range(ly-1):
    y_length.append(y_cut[i+1]-y_cut[i])

ans = 0
for a in x_length:
    for b in y_length:
        ans = max(ans, a*b)
print(ans)
