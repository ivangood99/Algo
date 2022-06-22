# from math import sqrt
#
# EPS = 10 ** (-4)
# N_ITERATIONS = 100
#
# def count_time(a, x):
#     time_p = sqrt(x ** 2 + (1 - a) ** 2) / speed_p
#     time_f = sqrt((1 - x) ** 2 + a ** 2) / speed_f
#     return time_p + time_f
#
#
# def solve(a):
#     left = 0
#     right = 1
#     for _ in range(N_ITERATIONS):
#         #m1 = left + (right - left) / 3
#         #m2 = m1 + (right - left) / 3
#         m = (left + right) / 2
#         m1 = m - EPS
#         m2 = m + EPS
#         if count_time(a, m1) > count_time(a, m2):
#             left = m1
#         else:
#             right = m2
#     return right
#
# speed_p, speed_f = map(int, input().split())
# a = float(input())
# print(solve(a))


a = input()
b = input()

flg = False
l = 0
r = 0

if b == '':
    print('YES')

else:
    for i in range(len(a)):
        if b[0] == a[i]:
            l = i

        if (len(b) > 1) and (a[i] == b[1]):
            r = i
            break

    if len(b) == 1:
        if a[l] == b[0]:
            print('YES')
        else:
            print('NO')

    elif r != 0:
        k = 2
        for i in range(2 * r - l, len(b)*r - l, r - l):
            if (k < len(b)) and (b[k] == a[i]):
                k += 1
        if k != len(b):
            print('NO')

        else:
            print('YES')
    else:
        print('NO')
