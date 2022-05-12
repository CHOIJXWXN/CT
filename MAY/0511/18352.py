'''
특정 거리의 도시 찾기
'''
from collections import deque
import sys

read = sys.stdin.readline
N, M, K, X = map(int, read().split())
G = [list() for _ in range(N + 1)]
v = [False] * (N + 1)
for _ in range(M):
    A, B = map(int, read().split())
    G[A].append(B)
q = deque()
cnt = 0
q.append(X)
v[X] = True
while q:
    if cnt == K:
        break
    lenQ = len(q)
    for _ in range(lenQ):
        x = q.popleft()
        for next in G[x]:
            if not v[next]:
                v[next] = True
                q.append(next)
    cnt += 1
print(*sorted(q), sep='\n') if q else print(-1)