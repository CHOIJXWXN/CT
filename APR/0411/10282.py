'''
해킹
'''
from heapq import heappop, heappush
import sys

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    conn = [list() for _ in range(n + 1)]
    # conn = [[10**7] * (n + 1) for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        conn[b].append([s, a])
        # conn[b][a] = s
    d = [10**7] * (n + 1)
    q = []
    heappush(q, [0, c])
    d[c] = 0
    while q:
        t, i = heappop(q)
        for time, ni in conn[i]:
            nt = t + time
            if nt < d[ni]:
                d[ni] = nt
                heappush(q, [nt, ni])
    cnt, S = 0, 0
    for D in d:
        if D != 10**7:
            cnt += 1
            S = max(S, D)
    print(cnt, S)
    # for k in range(1, n + 1):
    #     for i in range(1, n + 1):
    #         for j in range(1, n + 1):
    #             conn[i][j] = min(conn[i][j], conn[i][k] + conn[k][j])
    # print(conn[c])