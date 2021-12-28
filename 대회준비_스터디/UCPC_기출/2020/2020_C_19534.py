"""
# sol1: index 오류
import sys
sys.setrecursionlimit(10**6)


def evalValue(string):
    return int(string)


def evalCondition(string):
    value1, value2 = string[0], string[-1]  # 길이 1로 고정
    return int(value1 == value2)


def evalExpression(string):
    length = len(string)
    if length == 1:
        return evalValue(string)

    stack = []
    breaker = False
    for i in range(length):
        if string[i] == '?':
            if len(stack) > 0:
                q_idx = stack[-1][1]
                breaker = True
                break
            else:
                stack.append(('?', i))
        if string[i] == ':':
            stack.pop()
    if not breaker:  # 중간에 종료하지 않았다면 <=> 즉, ? 다음에 ?인 경우가 없었다면
        for i in range(length):
            if string[i] == '?':
                q_idx = i
                break

    stack = []
    breaker = False
    for i in range(length-1, -1, -1):
        if string[i] == ':':
            if len(stack) > 0:
                c_idx = stack[-1][1]
                breaker = True
                break
            else:
                stack.append((':', i))
        if string[i] == '?':
            stack.pop()  # 앞이 ':'일 수 없음 // 이전에 있을 '?'에 의해 pop 당하기 때문
    if not breaker:
        for i in range(length-1, -1, -1):
            if string[i] == ':':
                c_idx = i
                break
    cond, exp1, exp2 = string[:q_idx], string[q_idx+1:c_idx], string[c_idx+1:]

    if evalCondition(cond):
        return evalExpression(exp1)
    else:
        return evalExpression(exp2)


def Dfs(string, ith_alphabet, zero_one, n):  # 문자열, 몇번재 알파벳을, 0 또는 1로 바꿀지, n번째 까지 바꾸면 종료
    if ith_alphabet == n+1:  # n이 아니라 n+1이 종료조건이므로 2번씩 중복 카운트
        if evalExpression(string) == 0:
            global ans
            ans += 1
        return
    global l, ithAlpha
    for i in range(l):
        if string[i] == ithAlpha[ith_alphabet]:
            string = string[:i] + zero_one + string[i+1:]
    Dfs(string, ith_alphabet+1, '0', n)
    Dfs(string, ith_alphabet+1, '1', n)


N = int(input())
s = input()
l = len(s)
ithAlpha = {}  # 수 - 영어 소문자
for i in range(26):
    ithAlpha[i+1] = chr(i+97)  # 97=a, ..., 122=z

ans = 0
Dfs(s, 1, '0', N)
Dfs(s, 1, '1', N)
print(ans//2)

# sol2: 시간 초과
import sys
sys.setrecursionlimit(10**6)


def evalValue(string):
    return int(string)


def evalCondition(string):
    value1, value2 = string[0], string[-1]  # 길이 1로 고정
    return int(value1 == value2)


def evalExpression(string):
    length = len(string)
    if length == 1:
        return evalValue(string)
    # q_idx와 c_idx 찾는 부분 수정함
    find_question = False
    stack = 0
    for i in range(length):
        if string[i] == '?':
            stack += 1
        if string[i] == ':':
            stack -= 1
        if not find_question and string[i] == '?':
            q_idx = i  # 첫 ? 가 가장 큰 범위의 (?, :) 쌍에 해당하는 '?'
            find_question = True
        if find_question and stack == 0:
            # '?' 와 ':'를 각각 '(' 와 ')'라고 생각했을 때, q_idx의 ?에 대응하는 '(' 와 짝을 이루는 ')'에 해당하는 ':'의 index 가 q_idx
            c_idx = i
            break

    cond, exp1, exp2 = string[:q_idx], string[q_idx+1:c_idx], string[c_idx+1:]

    if evalCondition(cond):
        return evalExpression(exp1)
    else:
        return evalExpression(exp2)


def Dfs(string, ith_alphabet, zero_one, n):  # 문자열, 몇번재 알파벳을, 0 또는 1로 바꿀지, n번째 까지 바꾸면 종료
    if ith_alphabet == n+1:  # n이 아니라 n+1이 종료조건이므로 2번씩 중복 카운트
        if evalExpression(string) == 0:
            global ans
            ans += 1
        return
    global l, ithAlpha
    for i in range(l):
        if string[i] == ithAlpha[ith_alphabet]:
            string = string[:i] + zero_one + string[i+1:]
    Dfs(string, ith_alphabet+1, '0', n)
    Dfs(string, ith_alphabet+1, '1', n)


N = int(input())
s = input()
l = len(s)
ithAlpha = {}  # 수 - 영어 소문자
for i in range(26):
    ithAlpha[i+1] = chr(i+97)  # 97=a, ..., 122=z

ans = 0
Dfs(s, 1, '0', N)
Dfs(s, 1, '1', N)
print(ans//2)

# sol3: 시간초과
import sys
sys.setrecursionlimit(10**6)


def evalValue(string):
    return int(string)


def evalCondition(string, start, finish):
    value1, value2 = string[start], string[finish]
    return int(value1 == value2)


def evalExpression(string, start, finish):
    length = finish - start + 1
    if length == 1:
        return evalValue(string[start])

    find_question = False
    stack = 0
    for i in range(start, finish + 1):
        if string[i] == '?':
            stack += 1
        if string[i] == ':':
            stack -= 1
        if not find_question and string[i] == '?':
            q_idx = i
            find_question = True
        if find_question and stack == 0:
            # '?' 와 ':'를 각각 '(' 와 ')'라고 생각했을 때, q_idx의 ?에 대응하는 '(' 와 짝을 이루는 ')'에 해당하는 ':'의 index 가 q_idx
            c_idx = i
            break

    if evalCondition(string, start, q_idx-1):
        return evalExpression(string, q_idx+1, c_idx-1)
    else:
        return evalExpression(string, c_idx+1, finish)


def Dfs(string, ith_alphabet, zero_one, n):
    if ith_alphabet == n+1:
        if evalExpression(string, 0, len(string)-1) == 0:
            global ans
            ans += 1
        return
    global l, ithAlpha
    for i in range(l):
        if string[i] == ithAlpha[ith_alphabet]:
            string = string[:i] + zero_one + string[i+1:]
    Dfs(string, ith_alphabet+1, '0', n)
    Dfs(string, ith_alphabet+1, '1', n)


N = int(input())
s = input()
l = len(s)
ithAlpha = {}  # 수 - 영어 소문자
for i in range(26):
    ithAlpha[i+1] = chr(i+97)  # 97=a, ..., 122=z

ans = 0
Dfs(s, 1, '0', N)
Dfs(s, 1, '1', N)
print(ans//2)
"""
# sol4: 간략화 but 시간초과
import sys
sys.setrecursionlimit(10**6)


def evalExpression(string, start, finish):  # 문자열, 시작 인덱스, 끝 인덱스
    length = finish - start + 1
    if length == 1:
        return int(string[start])

    q_idx = start + 4  # A==B?~
    stack = 1
    for i in range(q_idx + 1, finish + 1):
        if string[i] == '?':
            stack += 1
        if string[i] == ':':
            stack -= 1
        if stack == 0:
            c_idx = i
            break
    if string[start] == string[q_idx-1]:
        return evalExpression(string, q_idx+1, c_idx-1)
    else:
        return evalExpression(string, c_idx+1, finish)


def Dfs(string, length, ith_alphabet, zero_one, n):  # 문자열, 문자열의 길이, 몇번재 알파벳을, 0 또는 1로 바꿀지, n번째 까지 바꾸면 종료
    if ith_alphabet == n+1:  # n이 아니라 n+1이 종료조건이므로 2번씩 중복 카운트
        if evalExpression(string, 0, l-1) == 0:
            global ans
            ans += 1
        return
    global ithAlpha
    for i in range(length):
        if string[i] == ithAlpha[ith_alphabet]:
            string = string[:i] + zero_one + string[i+1:]  # 시간복잡도가..
    Dfs(string, length, ith_alphabet+1, '0', n)
    Dfs(string, length, ith_alphabet+1, '1', n)


N = int(input())
s = input()
l = len(s)

ithAlpha = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
ans = 0
Dfs(s, l, 1, '0', N)
Dfs(s, l, 1, '1', N)
print(ans // 2)

# a==b?c==d?e:f:g
# 1==1?1==1?0:1:1==0?0:0
# 1==1  ?  1==1?0:1  :  1==0?0:0
# 1==1?1==1?1==1?1==1?0:0:0:0:0
