'''
가장 긴 증가하는 부분 수열 2
'''
# DP (시간초과)
# import sys

# read = sys.stdin.readline
# N = int(read())
# A = list(map(int, read().split()))
# d = [1] * N
# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             d[i] = max(d[i], d[j] + 1)
# print(max(d))

'''
5   
10 50 5 8 40
'''
# 이분탐색 (구글링함)
import sys

read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))
d = [0]
for a in A:
    if d[-1] < a:
        d.append(a)
    else:
        s, e = 0, len(d)
        while s < e:
            m = (s + e) // 2
            if d[m] < a:
                s = m + 1
            else:
                e = m
        print(d)
        print(e)
        d[e] = a
print(d)
print(len(d) - 1)