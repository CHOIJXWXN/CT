"""
너 봄에는 캡사이신이 맛있단다
"""

# s, e가 있다면
# s랑 e 사이에서 조합 개수 => e - s + 1개 중 s와 e는 꼭 고름
# 2 ** (e - s - 1)

# import sys
# read = sys.stdin.readline
#
# N = int(read())
# S = list(map(int, read().split()))
# S.sort()
# cnt, MOD = 0, 1_000_000_007
# for s in range(N - 1):
#     for e in range(s, N):
#         cnt += int(2**(e - s - 1) * (S[e] - S[s])) % MOD
# print(cnt % MOD)

# 시간초과라서 2**x 부분을 분할정복으로 바꿨지만 그래도 시간초과

# import sys
# read = sys.stdin.readline
#
#
# def p(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 2
#     m = p(n // 2)
#     return m * m * 2 % MOD if n % 2 else m * m % MOD
#
#
# N = int(read())
# S = list(map(int, read().split()))
# S.sort()
# cnt, MOD = 0, 1_000_000_007
# for s in range(N - 1):
#     for e in range(s + 1, N):
#         cnt += (p(e - s - 1) * (S[e] - S[s])) % MOD
# print(cnt % MOD)

# 암만봐도 NlogN이 에바인 거 같아서

# import sys
# read = sys.stdin.readline
#
#
# def p(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 2
#     m = p(n // 2)
#     return m * m * 2 % MOD if n % 2 else m * m % MOD
#
#
# N = int(read())
# S = list(map(int, read().split()))
# S.sort()
# cnt, MOD = 0, 1_000_000_007
# for i in range(N):
#     cnt += S[i] * (p(i) - p(N - i - 1))
# print(cnt % MOD)

# 아니 pow 함수가 더 성능이 좋다고? 왜 분할 정복함?

import sys
read = sys.stdin.readline

N = int(read())
S = list(map(int, read().split()))
S.sort()
MOD = 1_000_000_007
cnt = sum(S[i] * (pow(2, i, MOD) - pow(2, N - i - 1, MOD)) for i in range(N))
print(cnt % MOD)

# MOD 때문인지는 몰라도 **가 성능이 더 별로임

# import sys
# read = sys.stdin.readline
#
# N = int(read())
# S = list(map(int, read().split()))
# S.sort()
# MOD = 1_000_000_007
# cnt = sum(S[i] * (2**i - 2**(N - i - 1)) % MOD for i in range(N))
# print(cnt % MOD)
