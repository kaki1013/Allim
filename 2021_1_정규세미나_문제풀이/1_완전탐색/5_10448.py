tri = []
for i in range(1, 46):
    tri.append(int(i * (i + 1) / 2))


def possible(n):
    for a in tri:
        for b in tri:
            for c in tri:
                if a + b + c == n:
                    return 1
    return 0


N = int(input())

for i in range(N):
    print(possible(int(input())))
