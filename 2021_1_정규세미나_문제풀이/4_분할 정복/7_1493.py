length, width, height = map(int, input().split())
N = int(input())
cube = []
for _ in range(N):
    cube.append(list(map(int, input().split())))
cube.sort()

def box(l,w,h):
    pass