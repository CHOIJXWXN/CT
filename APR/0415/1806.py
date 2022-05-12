'''
부분합
'''
import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
s, e = 0, 0
sum, l = a[s], N + 1
while s <= e:
    if sum >= S:
        l = min(l, e - s + 1)
        sum -= a[s]
        s += 1
    else:
        if e == N - 1:
            break
        e += 1
        sum += a[e]
print(l) if l < N + 1 else print(0)