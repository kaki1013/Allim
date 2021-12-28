def prime_deter(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def p_deter(n):
    x = list(str(n))
    if x == x[::-1]:
        return True
    return False


N = int(input())
while (not prime_deter(N)) or (not p_deter(N)):
    N += 1
print(N)