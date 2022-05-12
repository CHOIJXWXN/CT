'''
특정한 최단 경로
1 > v1 > v2 > N
1 > v2 > v1 > N
'''
# import sys

# N, E = map(int, input().split())
# mtx = [[10**6 for _ in range(N + 1)] for _ in range(N + 1)]
# for _ in range(E):
#     a, b, c = map(int, sys.stdin.readline().rstrip().split())
#     mtx[a][b] = mtx[b][a] = c
# v1, v2 = map(int, input().split())
# for k in range(N + 1):
#     for i in range(N + 1):
#         for j in range(N + 1):
#             mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j])
# print(min(mtx[1][v1] + mtx[v1][v2] + mtx[v2][N], mtx[1][v2] + mtx[v2][v1] + mtx[v1][N]))

from heapq import heappop, heappush
import sys

def min_d(I, F):
    q = []
    d = [10**7] * (N + 1)
    heappush(q, (0, I))
    while q:
        w, now = heappop(q)
        if now == F:
            return w
        for C in conn[now]:
            if d[C[0]] > w + C[1]:
                d[C[0]] = w + C[1]
                heappush(q, (d[C[0]], C[0]))
    return 10**7

N, E = map(int, input().split())
conn = [list() for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    conn[a].append([b, c])
    conn[b].append([a, c])
v1, v2 = map(int, input().split())
v11 = min_d(1, v1)
v12 = min_d(1, v2)
v1v2 = min_d(v1, v2)
v1n = min_d(v1, N)
v2n = min_d(v2, N)
ans = min(v11 + v1v2 + v2n, v12 + v1v2 + v1n)
print(ans) if ans < 10**7 else print('-1')