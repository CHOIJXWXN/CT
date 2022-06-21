"""
공항
"""

# 안 돌려봐도 시간초과될 거 같음

# import sys
# read = sys.stdin.readline
#
# G = int(read())
# P = int(read())
# T = [0] * (G + 1)
# for i in range(1, P + 1):
#     d = int(read())
#     for j in range(d, G + 1):
#         T[j] += 1
#     if T[d] > d:
#         print(i - 1)
#         exit()

import sys
read = sys.stdin.readline
# 1 3 3 5 5 5
#  0  1  2  3  4  5
# [0, 1, 0, 2, 0, 3]

G = int(read())
P = int(read())
for i in range(1, P + 1):
    d = int(read())
