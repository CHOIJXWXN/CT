'''
내려가기
'''
# import sys

# read = sys.stdin.readline
# N = int(read())
# S = list()
# for _ in range(N):
#     S.append(list(map(int, read().split())))
# minD, maxD = 10**6, 0
# for i in range(3):
#     dmin = [[10**6] * 3 for _ in range(N)]
#     dmax = [[-10**6] * 3 for _ in range(N)]
#     dmin[0][i] = dmax[0][i] = S[0][i]
#     for j in range(1, N):
#         dmin[j][0] = min(dmin[j - 1][0], dmin[j - 1][1]) + S[j][0]
#         dmin[j][1] = min(dmin[j - 1][0], dmin[j - 1][1], dmin[j - 1][2]) + S[j][1]
#         dmin[j][2] = min(dmin[j - 1][1], dmin[j - 1][2]) + S[j][2]
#         dmax[j][0] = max(dmax[j - 1][0], dmax[j - 1][1]) + S[j][0]
#         dmax[j][1] = max(dmax[j - 1][0], dmax[j - 1][1], dmax[j - 1][2]) + S[j][1]
#         dmax[j][2] = max(dmax[j - 1][1], dmax[j - 1][2]) + S[j][2]
#     minD = min(min(dmin[N - 1]), minD)
#     maxD = max(max(dmax[N - 1]), maxD)
# print(maxD, minD)


import sys

read = sys.stdin.readline
N = int(read())
maxL = list(map(int, read().split()))
minL = maxL[:]
for i in range(N - 1):
    L = list(map(int, read().split()))
    tmpMax = maxL[:]
    maxL[0] = max(tmpMax[0], tmpMax[1]) + L[0]
    maxL[1] = max(tmpMax[0], tmpMax[1], tmpMax[2]) + L[1]
    maxL[2] = max(tmpMax[1], tmpMax[2]) + L[2]
    tmpMin = minL[:]
    minL[0] = min(tmpMin[0], tmpMin[1]) + L[0]
    minL[1] = min(tmpMin[0], tmpMin[1], tmpMin[2]) + L[1]
    minL[2] = min(tmpMin[1], tmpMin[2]) + L[2]
print(max(maxL), min(minL))