'''
물 주기
'''
N, K, A, B = map(int, input().split())
pot = [K] * N
days = 0
while True:
    if pot.count(0):
        print(days)
        break
    for i in range((days * A) % N, ((days + 1) * A - 1) % N + 1):
        pot[i] += B
    for i in range(N):
        pot[i] -= 1
    days += 1