'''
숨바꼭질3
'''
from heapq import heappop, heappush

N, K = map(int, input().split())

# N이 K보다 크다면 항상 -1방향으로 가야하므로 답은 정해져있으므로 계산 후 프로그램 종료
if N > K:
    print(N - K)
    exit()

INF = 10**5 + 1
d = [INF] * INF
d[N] = 0
q = []
heappush(q, [0, N])
while q:
    t, x = heappop(q)
    for nx in [x - 1, x + 1, 2 * x]:
        if 0 <= nx < INF:
            if nx == 2 * x and d[nx] > t:
                d[nx] = t
                heappush(q, [t, nx])
            elif d[nx] > t + 1:
                d[nx] = t + 1
                heappush(q, [t + 1, nx])
print(d[K])