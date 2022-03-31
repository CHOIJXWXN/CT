'''
차이를 최대로
'''
# 브루트포스 / 라이브러리 사용
from itertools import permutations
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
max_tot = 0
for p in permutations(nums, N):
    tot = 0
    for i in range(N - 1):
        tot += abs(p[i] - p[i + 1])
    max_tot = max(max_tot, tot)
print(max_tot)