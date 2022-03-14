'''
완전제곱수
A^2 = B^2 + N
(A + B)(A - B) = N
N 인수분해 -> (1, N) ... 등의 쌍을 찾아 
'''
N = int(input())
cnt = 0
n = int(N ** 0.5) + 1 if int(N ** 0.5) != (N ** 0.5) else int(N ** 0.5)
for i in range(1, n):
    if not N % i:
        if not (i + (N // i)) % 2:
            cnt += 1
print(cnt)