'''
최소비용 구하기
'''
# import sys

# read = sys.stdin.readline
# N = int(read())
# M = int(read())
# mtx = [[10**5] * (N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     S, E, P = map(int, read().rstrip().split())
#     mtx[S][E] = P
# I, F = map(int, read().rstrip().split())
# for k in range(N + 1):
#     for i in range(N + 1):
#         for j in range(N + 1):
#             mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j])
# print(mtx[I][F])

from heapq import heappop, heappush
import sys

read = sys.stdin.readline
N = int(read())
M = int(read())
mtx = [list() for _ in range(N + 1)]
for _ in range(M):
    S, E, P = map(int, read().rstrip().split())
    mtx[S].append([E, P])
I, F = map(int, read().rstrip().split())
d = [10**9] * (N + 1)
q = []
heappush(q, (0, I))
while q:
    cost, now = heappop(q)
    if now == F:
        print(cost)
        break
    if d[now] < cost:
        continue
    for N in mtx[now]:
        if d[N[0]] > cost + N[1]:
            d[N[0]] = cost + N[1]
            heappush(q, (d[N[0]], N[0]))