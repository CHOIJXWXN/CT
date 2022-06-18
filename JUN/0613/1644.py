"""
소수의 연속합
자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력
"""

N = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    prime = [0] * 2 + [1] * (N - 1)
    p = list()
    p_num = 0
    for i in range(2, int(N ** (1/2)) + 1):
        if not prime[i]:
            continue
        for j in range(2, N // i + 1):
            prime[i * j] = 0
    for i in range(N + 1):
        if prime[i]:
            p.append(i)
            p_num += 1
    for i in range(p_num - 1):
        s, e = i, i + 1
        tot = p[s] + p[e]
        while tot <= N:
            prime[tot] += 1
            e += 1
            tot += p[e]
    print(prime[-1])