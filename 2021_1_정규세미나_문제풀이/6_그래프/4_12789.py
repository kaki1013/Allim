N = int(input())
line = list(map(int, input().split()))[::-1]

stack = []
turn = 1

while turn <= N:
    if len(line) > 0 and line[-1] == turn:
        line.pop()
        turn += 1
    elif len(stack) > 0 and stack[-1] == turn:
        stack.pop()
        turn += 1
    elif len(line) > 0:
        stack.append(line[-1])
        line.pop()
    else:
        break

if turn == N + 1:
    print('Nice')
else:
    print('Sad')
