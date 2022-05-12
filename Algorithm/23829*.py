'''
인문예술탐사주간
'''
import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())
P = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(Q):
    sum = 0
    x = int(sys.stdin.readline())
    for j in range(N):
        sum += abs(P[j] - x)
    print(sum)