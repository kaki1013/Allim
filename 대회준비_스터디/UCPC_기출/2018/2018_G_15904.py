s = input()
ans = 'UCPC'

s_idx, ans_idx = 0, 0
l = len(s)
while s_idx < l and ans_idx < 4:
    if s[s_idx] == ans[ans_idx]:
        ans_idx += 1
    s_idx += 1

print('I love UCPC' if ans_idx == 4 else 'I hate UCPC')

# https://www.acmicpc.net/source/13209931
# try, except 문 사용
import sys
ucpc = input()
try:
    ucpc = ucpc[ucpc.index('U'):]
    ucpc = ucpc[ucpc.index('C'):]
    ucpc = ucpc[ucpc.index('P'):]
    ucpc = ucpc[ucpc.index('C'):]
except:
    print("I hate UCPC")
    sys.exit()
print("I love UCPC")