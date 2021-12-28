import sys


def str_to_num(start, end):
    if start < 0 or end > len(num_list):
        return float('inf')
    multiply = 1
    rt_num = 0
    for i in range(end-1, start-1, -1):
        rt_num += num_list[i] * multiply
        multiply *= 10
    return rt_num


def solve():
    s1, s2, s3 = str_to_num(0, 1), str_to_num(0, 2), str_to_num(0, 3)
    e1, e2, e3 = str_to_num(len(num_list) - 1, len(num_list)), str_to_num(len(num_list) - 2, len(num_list)), str_to_num(len(num_list) - 3, len(num_list))
    if calc_len(e1) - calc_len(s1) + 1 == len(num_list):
        print(s1, e1)
    elif calc_len(e2) - calc_len(s1) + 1 == len(num_list):
        print(s1, e2)
    elif calc_len(e3) - calc_len(s1) + 1 == len(num_list):
        print(s1, e3)
    elif calc_len(e2) - calc_len(s2) + 2 == len(num_list):
        print(s2, e2)
    elif calc_len(e3) - calc_len(s2) + 2 == len(num_list):
        print(s2, e3)
    elif calc_len(e3) - calc_len(s3) + 3 == len(num_list):
        print(s3, e3)
    else:
        a, b = 1, 0
        c = a / b


def calc_len(num):
    if num < 10:
        return num
    elif num < 100:
        return 9 + (num - 9) * 2
    elif num < 1000:
        return 9 + 90 * 2 + (num - 99) * 3
    else:
        return float('inf')


num_list = list(map(int, list(sys.stdin.readline().strip())))
solve()