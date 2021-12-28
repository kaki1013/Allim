while True:
    N, M = map(int, input().split())  # str
    if (N, M) == (0, 0):
        break
    call_arr = []
    test_arr = []
    for _ in range(N):
        call_arr.append(list(map(int, input().split()))[2:])
    for _ in range(M):
        test_arr.append(list(map(int, input().split())))
    for scope in test_arr:
        count = 0
        for check in call_arr:
            if (sum(scope)-check[0]) * (sum(check)-scope[0]) > 0:
                count += 1
        print(count)