'''
보석 상자

RRRRRRR
BBBB

질투심 n > ceil(7/n) + ceil(4/n) 명 > M명보다 작으면
질투심 n-1 >
...

질투심 n > M명보다 크면
질투심 n + 1 > 
...
1   2   3   4   5
'''
# 평균값에서부터 하나씩 늘려가는 방법
# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# j = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
# i = sum(j) // N
# while True:
#     tot = 0
#     for J in j:
#         t = J // i + 1 if J % i else J // i
#         tot += t
#     if tot > N:
#         i += 1
#     else:
#         break
# print(i)

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
j = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
bottom = sum(j) // N
top = max(j)
while True:
    if bottom > top:
        break
    tot = 0
    m = (top + bottom) // 2
    for J in j:
        t = J // m + 1 if J % m else J // m
        tot += t
    if tot > N:
        bottom = m + 1
    else:
        top = m - 1
# print(m)
print(bottom)