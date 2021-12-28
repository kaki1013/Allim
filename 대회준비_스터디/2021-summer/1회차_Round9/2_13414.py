from sys import stdin
input = stdin.readline

K, L = map(int, input().strip().split())
wait = [input().strip() for _ in range(L)]

clicked = set()
clicked_dict = {}
checked_dict = {}

for i in range(L):
    if wait[i] not in clicked:
        clicked.add(wait[i])
        clicked_dict[wait[i]] = 1
        checked_dict[wait[i]] = 1
    else:
        clicked_dict[wait[i]] += 1

i = 0
while K != 0 and i < L:  # 다 뽑지 않았고 정원이 더 많은 경우
    if clicked_dict[wait[i]] == checked_dict[wait[i]]:  # 가장 마지막
        print(wait[i])
        K -= 1
    else:  # 뒤에 클릭이 더 있음
        checked_dict[wait[i]] += 1
    i += 1
