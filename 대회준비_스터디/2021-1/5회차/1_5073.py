import sys

arr = []
for line in sys.stdin:
    ll = list(map(int, line.strip().split()))
    if ll == [0, 0, 0]:
        break
    else:
        arr.append(ll)

for nums in arr:
    nums.sort()
    a, b, c = nums[2], nums[1], nums[0]
    if (a, b, c) == (0, 0, 0):
        break
    if a >= b + c:
        print("Invalid")
    else:
        s = set(nums)
        l = len(s)
        if l == 1:
            print("Equilateral")
        elif l == 2:
            print("Isosceles")
        else:
            print("Scalene")
