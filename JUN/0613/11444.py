"""
피보나치 수 6
f(1) = 1
f(2) = 2
f(3) = 3
f(4) = 5
f(5) = 8
f(6) = 13

f(n) = f(n - 1) + f(n - 2)
f(n + 1) = f(n) + f(n - 1)
         = 2 * f(n - 1) + f(n - 2)
f(n + 2) = f(n + 1) + f(n)
         = 2 * f(n - 1) + f(n - 2) + f(n)
         = 3 * f(n - 1) + 2 * f(n - 2)
f(n + 3) = f(n + 2) + f(n + 1)
         = 3 * f(n - 1) + 2 * f(n - 2) + f(n + 1)
         = 5 * f(n - 1) + 3 * f(n - 2)
f(n + a) = f(a + 1) * f(n - 1) + f(a) * f(n - 2)

f(n + n) = f(n + 1) * f(n - 1) + f(n) * f(n - 2)
f(n + n) = f(n)f(n - 1) + f(n - 1)**2 + f(n)f(n - 2)
         = f(n)f(n) + f(n-1)f(n-1)

=> f(2n) = f(n)^2 + f(n-1)^2

f(n + n - 1) = f(n) * f(n - 1) + f(n - 1) * f(n - 2)

=> f(2n - 1) = f(n)^2 - f(n-2)^2
"""
# MOD = 1_000_000_007
#
# def fibo(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n % 2:
#         return ((fibo(n // 2 + 1) % MOD) ** 2) % MOD - ((fibo(n // 2 - 1) % MOD) ** 2) % MOD
#     else:
#         return ((fibo(n // 2) % MOD) ** 2) % MOD + ((fibo(n // 2 - 1) % MOD) ** 2) % MOD
#
#
# N = int(input())
# print(fibo(N - 1) % MOD)


# 행렬 계산

MOD = 1_000_000_007


def fibo(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    else:
        mtx1 = fibo(n // 2)
        mtx2 = [[0, 0], [0, 0]]
        mtx2[0][0] = (mtx1[0][0] * mtx1[0][0] + mtx1[0][1] * mtx1[1][0]) % MOD
        mtx2[0][1] = (mtx1[0][0] * mtx1[0][1] + mtx1[0][1] * mtx1[1][1]) % MOD
        mtx2[1][0] = (mtx1[1][0] * mtx1[0][0] + mtx1[1][1] * mtx1[1][0]) % MOD
        mtx2[1][1] = (mtx1[1][0] * mtx1[0][1] + mtx1[1][1] * mtx1[1][1]) % MOD
        if n % 2:
            mtx1[0][0] = (mtx2[0][0] + mtx2[1][0]) % MOD
            mtx1[0][1] = (mtx2[0][1] + mtx2[1][1]) % MOD
            mtx1[1][0] = mtx2[0][0]
            mtx1[1][1] = mtx2[0][1]
            return mtx1
        return mtx2


N = int(input())
mtx = fibo(N)
print(mtx[0][1])

# 68ms 코드 =========================================================================


def matrix_multiplication(a, b, mod):
    return [[(a[0][0] * b[0][0] % mod + a[0][1] * b[1][0] % mod) % mod,
             (a[0][0] * b[0][1] % mod + a[0][1] * b[1][1] % mod) % mod],
            [(a[1][0] * b[0][0] % mod + a[1][1] * b[1][0] % mod) % mod,
             (a[1][0] * b[0][1] % mod + a[1][1] * b[1][1] % mod) % mod]]


def find_fibonacci_num(n, mod):
    if not n:
        return 0
    ans = [[1, 0], [0, 1]]
    q = [[1, 1], [1, 0]]
    while n > 0:
        if n % 2:
            ans = matrix_multiplication(q, ans, mod)
        q = matrix_multiplication(q, q, mod)
        n //= 2
    return ans[1][0]


n = int(input())
print(find_fibonacci_num(n, 10**9 + 7))