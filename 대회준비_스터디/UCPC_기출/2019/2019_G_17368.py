# 교점세기_미해결
import sys
# sys.stdin.readline().rstrip()

n = int(input())

lines, hyps, exps = [], [], []
for _ in range(n):
    operator, a = input().split()
    a = int(a)
    if operator == '*':
        lines.append(a)
    elif operator == '/':
        hyps.append(a)
    elif operator == '^':
        exps.append(a)

ans = 0

l, e = len(lines), len(exps)
if l >=2 or l == 1 and 0 in lines:
    ans += 1  # 0, 0
if e >= 2:
    ans += 1  # 0, 1

line_hyper = set()
line_exp = set()
hyper_exp = set()

for line in lines:
    for hyp in hyps:
        pass
