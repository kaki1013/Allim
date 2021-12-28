s = input()
split = s.split('.')

impossible = False
for i in range(len(split)):
    if split[i] == '':
        continue
    l = len(split[i])
    if l % 2 == 1:
        impossible = True
        break
    split[i] = 'AAAA' * (l//4) + 'B' * (l%4)

if impossible:
    print(-1)
else:
    print('.'.join(split))
