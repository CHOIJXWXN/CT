'''
신입사원
'''
# from heapq import heappop, heappush
# import sys

# read = sys.stdin.readline
# T = int(read())
# for _ in range(T):
#     N = int(read())
#     E = list()
#     for _ in range(N):
#         heappush(E, list(map(int, read().split())))
#     limit, cnt = heappop(E)[1], 1
#     for i in range(N - 1):
#         e = heappop(E)[1]
#         if limit > e:
#             limit = e
#             cnt += 1
#     print(cnt)


# 백준 채점 상
# 1. sorted보다는 sort
# 2. rstrip() 제거
# 3. 왠지 모르겠는데 힙큐가 더 느림(?)
# 4. 왠지 모르겠는데 pypy가 더 느림(????)

import sys

read = sys.stdin.readline
T = int(read())
for _ in range(T):
    N = int(read())
    E = list(list(map(int, read().split())) for _ in range(N))
    E.sort()
    limit, cnt = E[0][1], 1
    for i in range(1, N):
        if limit > E[i][1]:
            limit = E[i][1]
            cnt += 1
    print(cnt)