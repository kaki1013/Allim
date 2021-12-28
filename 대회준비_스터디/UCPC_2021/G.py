# 실패
# 2000 이상의 소수로 하면 된다고 함
K, N = map(int, input().split())
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
ans = []

for i in range(K):
    ans.append(list(range(prime[i], N*prime[i]+1, prime[i])))

for line in ans:
    print(*line)

a = ans[0]
b = ans[1]
c = ans[2]
d = ans[3]
s1 = set()
s2 = set()
s3 = set()
s4 = set()
s5 = set()
s6 = set()

for i in range(4):
    for j in range(4):
        s1.add(a[i] + b[j])
        s2.add(c[i] + b[j])
        s3.add(a[i] + c[j])
        s4.add(a[i] + d[j])
        s5.add(b[i] + d[j])
        s6.add(c[i] + d[j])
print(len(s1), len(s2), len(s3))
print(len(s4), len(s5), len(s6))
