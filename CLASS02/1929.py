'''
소수 구하기
'''
# M, N = map(int, input().split())
# for i in range(M, N + 1):
#     flag = True
#     max_d = int(i ** (1/2))
#     for j in range(2, max_d + 1):
#         if i % j == 0 and i != j:
#             flag = False
#             break
#     if flag and i != 1:
#         print(i)

M, N = map(int, input().split())

def isPrime(n):
    prime = [True] * (n + 1)
    prime[1] = False
    for i in range(2, int(n ** (1/2)) + 1):
        if prime[i] == True:
            j = 2
            while i * j <= n:
                prime[i * j] = False
                j += 1
    return prime

ans = isPrime(N)
for i in range(M, N + 1):
    if ans[i]:
        print(i)