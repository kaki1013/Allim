# 맞았습니다
n, T = map(int, input().split())
time_arr = list(map(int, input().split()))
used_time = 0
count = 0

while True:
    if used_time < T < used_time + time_arr[count]:
        break
    if count + 1 == n and used_time + time_arr[count] < T or T == used_time + time_arr[count]:
        count += 1
        break
    used_time += time_arr[count]
    count += 1

print(count)


# 맞았습니다
n, T = map(int, input().split())
time_arr = list(map(int, input().split()))
used_time = 0
count = 0

for time in time_arr:
    update_time = used_time + time
    if update_time > T or count == n:
        break
    count += 1
    used_time = update_time

print(count)
