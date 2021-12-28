import heapq
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    m1 = heapq.heappop(cards)
    m2 = heapq.heappop(cards)
    heapq.heappush(cards, m1 + m2)
    heapq.heappush(cards, m1 + m2)

print(sum(cards))
