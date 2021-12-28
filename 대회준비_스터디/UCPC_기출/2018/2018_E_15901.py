# 실패_단순 구현 X
from collections import deque
import sys

N, M, K, Q = map(int, sys.stdin.readline().rstrip().split())
wait = deque(list(map(int, sys.stdin.readline().rstrip().split())))
cmds = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(Q)]

fire = [0] * M
for i in range(min(N, M)):
    fire[i] = wait.popleft()

print_list = []
for cmd in cmds:
    if cmd[0] == 1:
        L, R = cmd[1] - 1, cmd[2] - 1
        wait_len = len(wait)
        for i in range(L, R + 1):
            fire[i] = 0
            if i - L < wait_len:
                fire[i] = wait.popleft()
    elif cmd[0] == 2:
        i = cmd[1] - 1
        print_list.append(fire[i])
    elif cmd[0] == 3:
        p, q = cmd[1], cmd[2]
        for _ in range(q):
            wait.append(p)
    elif cmd[0] == 4:
        t = cmd[1]
        for _ in range(t):
            wait.popleft()

print(*print_list)
print(*fire)
