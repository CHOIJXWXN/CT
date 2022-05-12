'''
파티
'''
from heapq import heappop, heappush

def dijkstra(mtx, F):
    d = [10**5] * (N + 1)
    d[F] = 0
    heappush(q, [d[F], F])
    while q:
        dis, idx = heappop(q)
        for i in range(1, N + 1):
            # 현재 마을과 i마을이 연결되어 있으며, 현재 i로 가는 거리가 idx를 거쳐 i로 가는 거리보다 클 때
            if mtx[idx][i] != 0 and d[i] > dis + mtx[idx][i]:
                d[i] = dis + mtx[idx][i]
                heappush(q, [d[i], i])
    return d

N, M, X = map(int, input().split())
fromto = [[0] * (N + 1) for _ in range(N + 1)]
tofrom = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, f, t = map(int, input().split())
    fromto[i][f] = t
    tofrom[f][i] = t
q = []
d1 = dijkstra(fromto, X)
d2 = dijkstra(tofrom, X)
max_tot = 0
for i in range(1, N + 1):
    max_tot = max(max_tot, d1[i] + d2[i])
print(max_tot)