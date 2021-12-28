import sys
sys.setrecursionlimit(10**5)


def palindrome(string, first):
    l = len(string) - 1
    i = 0
    if l == 1:  # abc가 재귀로, ab나 bc가 되어 온 경우를 제외하기 위함
        if string[0] == string[1]:
            return 0
        return 1
    while i < l // 2:
        if string[i] != string[l-i]:  # 양끝에서 시작하여 달라지는 인덱스 찾음
            break
        i += 1
    if i == l//2 and string[i] == string[l-i]:
        return 0
    elif first and (palindrome(string[i:l-i], False) == 0 or palindrome(string[i+1:l-i+1], False) == 0):
        return 1
    return 2


T = int(input())
for _ in range(T):
    print(palindrome(input(), True))