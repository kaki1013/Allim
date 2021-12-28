import sys
import heapq

stone_num = int(sys.stdin.readline())
stone_color = list(sys.stdin.readline().strip())

weight_list = list(map(int, sys.stdin.readline().split()))
weights = [weight_list[0]]

for i in range(1, stone_num):
    if stone_color[i - 1] == stone_color[i]:
        weights[-1] = max(weights[-1], weight_list[i])
    else:
        weights.append(weight_list[i])

if len(weights) <= 2:
    print("0")
else:
    weight_heap = weights[1:len(weights) - 1]
    heapq.heapify(weight_heap)
    w_sum = sum(weight_heap)
    for c in range(len(weight_heap) // 2):
        w_sum -= heapq.heappop(weight_heap)
    print(w_sum)