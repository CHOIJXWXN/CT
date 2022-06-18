"""
1의 개수 세기

홀수 규칙
f(2n + 1) = f(2n) + 1
짝수 규칙
f(2^n + 2m) = f(2^n) + f(2m) = 1 + f(2m)

0부터 3(11)까지
총 4개의 수
2 * 2 = 4

0부터 7(111)까지
총 8개의 수
4 * 3 = 12

0부터 15(1111)까지
총 16개의 수
8 * 4 = 32

0부터 31(11111)까지
총 32개의 수
16 * 5 = 80
"""
# from math import log2
#
#
# def one(n):
#     if n <= 0:
#         return 0
#     m = int(log2(n))
#     d = n - 2 ** m
#     if not d:
#         return m * n // 2 + 1
#     return one(n - d) + d + one(d)
#
#
# A, B = map(int, input().split())
# print(one(B) - one(A - 1))


import sys
input = sys.stdin.readline


def acc_one_nums(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    # log를 구하는 빠른 방법 ============================
    len_x = len(bin(x)) - 2
    # ==============================================
    return x - 2 ** (len_x - 1) + 1 + acc_one_nums(x - 2 ** (len_x - 1)) + (len_x - 1) * 2**(len_x - 2)


a, b = map(int, input().split())
print(acc_one_nums(b) - acc_one_nums(a - 1))