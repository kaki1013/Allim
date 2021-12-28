L = int(input())
N = int(input())
wish_list = []
for _ in range(N):
    wish_list.append(list(map(int, input().split())))

longest_wish = 1
wish_len = wish_list[0][1] - wish_list[0][0] + 1
for i in range(1, N):
    if wish_list[i][1] - wish_list[i][0] + 1> wish_len:
        wish_len = wish_list[i][1] - wish_list[i][0] + 1  # 최대값 업데이트 안했음
        longest_wish = i + 1
print(longest_wish)

cake_arr = [0] * (L + 1)
count_list = [0] * (N + 1)
for i in range(N):
    s, f = wish_list[i][0], wish_list[i][1]
    count = 0
    for ind in range(s, f + 1):
        if cake_arr[ind] == 0:
            cake_arr[ind] = i+1
            count += 1
    count_list[i + 1] = count
print(count_list.index(max(count_list)))

#m = max(count_list)
#for i in range(N + 1):
#    if count_list[i] == m:
#        print(i, end=' ')