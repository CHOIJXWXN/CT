"""
GCD(n, k) = 1
"""
N = int(input())
now, cnt = N, N
for i in range(2, int(N**0.5) + 1):
    if not now % i:
        while not now % i:
            now //= i
        cnt *= (1 - 1/i)
if now > 1:
    cnt *= (1 - 1/now)
print(int(cnt))
