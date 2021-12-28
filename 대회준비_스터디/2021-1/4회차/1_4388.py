while True:
    N, M = input().split()
    if (N, M) == ('0', '0'):
        break
    # 9999 11 - 10 - 11 - 10 - 10 (10010)4번
    if len(N) > len(M):
        M = '0'* (len(N) - len(M)) + M
    elif len(N) < len(M):
        N = '0'* (len(M) - len(N)) + N
    count = 0
    c = 0
    for n in range(len(N)):
        c = (int(N[-1-n]) + int(M[-1-n]) + c) // 10
        if c == 1:
            count += 1
    print(count)