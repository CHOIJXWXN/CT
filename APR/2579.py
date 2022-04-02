'''
계단 오르기
'''

# from pprint import pprint
# import sys

# read = sys.stdin.readline
# N = int(read().rstrip())
# scores = [int(read().rstrip()) for _ in range(N)]
# tot = [list() for _ in range(N)]
# tot[0].append([scores[0], False])
# for i in range(N - 2):
#     for t in tot[i]:
#         if not t[1]:
#             tot[i + 1].append([t[0] + scores[i + 1], True])
#         tot[i + 2].append([t[0] + scores[i + 2], False])
# max_t = 0
# for t in tot[N - 1]:
#     max_t = max(t[0], max_t)
# pprint(tot)
# print(max_t)


import sys

read = sys.stdin.readline
N = int(read().rstrip())
scores = [int(read().rstrip()) for _ in range(N)]
if N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
else:
    tot = [0] * N
    tot[0] = scores[0]
    tot[1] = scores[0] + scores[1]
    tot[2] = max(scores[0], scores[1]) + scores[2]
    for i in range(3, N):
        tot[i] = max(tot[i - 2] + scores[i], tot[i - 3] + scores[i - 1] + scores[i])
    print(tot[-1])

'''
scores
1  2  3  4  5
A  B  C  D  E

tot
1  2  3  4  5
a  b  c  d  e

e = 둘 중 하나 (d를 포함하느냐 안하느냐)
1. c + E
2. b + D + E
'''