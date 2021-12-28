import heapq
import sys


N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

ans = 0
while len(heap) > 1:
    m1 = heapq.heappop(heap)
    m2 = heapq.heappop(heap)
    heapq.heappush(heap, m1+m2)
    ans += m1 + m2

print(ans)