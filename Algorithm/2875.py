'''
대회 or 인턴
'''
N, M, K = map(int, input().split())
T = min(N // 2, M)
R = N + M - 3 * T
if K > R:
    T -= (K - R - 1) // 3 + 1
print(T)