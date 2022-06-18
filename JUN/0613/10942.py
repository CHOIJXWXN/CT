"""
팰린드롬?
"""

# 시간 초과

# import sys
#
# read = sys.stdin.readline
#
# N = int(read())
# nums = list(map(int, read().split()))
# M = int(read())
# for _ in range(M):
#     S, E = map(int, read().split())
#     flag = 1
#     while S < E:
#         if nums[S - 1] == nums[E - 1]:
#             S += 1
#             E -= 1
#             continue
#         else:
#             flag = 0
#             break
#     print(flag)

# DP

import sys

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
flag = [[0] * N for _ in range(N)]
for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if i == j:
            flag[i][j] = 1
        elif nums[i] == nums[j]:
            if i + 1 == j:
                flag[i][j] = 1
            if i < N - 1 and j > 0 and flag[i + 1][j - 1]:
                flag[i][j] = 1
M = int(read())
for _ in range(M):
    S, E = map(int, read().split())
    print(flag[S - 1][E - 1])
