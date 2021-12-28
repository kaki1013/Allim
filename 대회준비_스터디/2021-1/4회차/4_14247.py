# 무조건 느린 애부터 다 캐는게 이득 // why?
# 1 1 1/1 1 100일 때 1 101 100보다 1 2 201 이 이득
# 첫번째 날 + 네번째 날에 베는 양 = 네번째 날 한번에 베는 양
# 따라서 모든 나무 한번씩 캐야 함
# 즉 모든 나무를, 성장 속도 작은 것부터 캐는 그리디가 정답
n = int(input())
initial = list(map(int, input().split()))
grow = list(map(int, input().split()))

grow.sort()

cut = sum(initial)
for i in range(n):
    cut += i * grow[i]
print(cut)