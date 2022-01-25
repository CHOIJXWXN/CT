N, K = map(int, input().split())

def jul(n, k):
    if n == 1:
        return 1
    else:
        return (jul(n-1, k) + k - 1) % n + 1

print(jul(N, K))