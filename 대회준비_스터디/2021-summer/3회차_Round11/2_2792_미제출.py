# 참고: https://develoger.kr/2792%EB%B2%88-%EB%B3%B4%EC%84%9D%EC%83%81%EC%9E%90/
# 질투심이 최소일 때, 이때의 질투심을 k라고 하면, 즉 최대 보석 개수가 k라고 하면
# k 보다 큰 질투심을 가지도록 하는 경우가 존재. 다시 말해, k를 기준으로 참, 거짓이 나뉨 // 매개변수 탐색(파라메트릭 서치)
# 정답인지 판별할 때는, 색깔별로 최대 k개씩 가지고 (각 색깔별로) 남는 보석이 존재한다면 1명이 가지는 방식으로 배분
from sys import stdin
from math import ceil

N, M = map(int, input().split())
arr = [int(stdin.readline()) for _ in range(M)]

start, end, ans = 1, M, 0
while start <= end:
    mid, sections = (start + end) // 2, 0
    for i in arr:
        sections += ceil(i / mid)
    if sections <= N:
        ans, end = mid, mid - 1
    else:
        start = mid + 1

print(ans)
