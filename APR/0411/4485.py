'''
녹색 옷 입은 애가 젤다지?
'''
from heapq import heappop, heappush
import sys

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = 1
while True:
    N = int(input())
    if not N:
        break
    mtx = list()
    tot = list()
    pq = list()
    for _ in range(N):
        mtx.append(list(map(int, sys.stdin.readline().rstrip().split())))
        tot.append([10**7] * N)
    tot[0][0] = mtx[0][0]
    heappush(pq, (tot[0][0], 0, 0)) # rupee, r, c
    while pq:
        now, r, c = heappop(pq)
        for i in range(4):
            nr, nc = r + d[i][0], c + d[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                if tot[nr][nc] > mtx[nr][nc] + now:
                    tot[nr][nc] = mtx[nr][nc] + now
                    heappush(pq, (tot[nr][nc], nr, nc))
    print(f'Problem {T}: {tot[N - 1][N - 1]}')
    T += 1