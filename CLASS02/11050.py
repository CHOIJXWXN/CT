N, K = map(int, input().split())
denominator = 1
numerator = 1
for i in range(K):
    denominator *= N
    numerator *= K
    N -= 1
    K -= 1
print(denominator//numerator)