import sys

# ENWS = 0123(L:-1, R:+1)

A, B = map(int, input().split())
N, M = map(int, input().split())
positions = [(0, 0)]
directions = [0]
for _ in range(N):
    x, y, direction = input().split()
    positions.append((int(x), int(y)))
    if direction == 'E':
        direction = 0
    elif direction == 'N':
        direction = 1
    elif direction == 'W':
        direction = 2
    elif direction == 'S':
        direction = 3
    directions.append(direction)
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cmdS = [input().split() for _ in range(M)]
print(positions, directions, cmdS)
for i in range(M):
    robot, cmd, repeat = int(cmdS[i][0]), cmdS[i][1], int(cmdS[i][2])
    if cmd == 'L':
        pass
    x, y = positions[robot]
    if not (1 <= x + repeat * direct[cmd][0] <= A and 1 <= y + repeat * direct[cmd][1] <= B):
        print(f'Robot {robot} crashes into the wall')

