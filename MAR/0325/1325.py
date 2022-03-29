'''
효율적인 해킹
이게 최선인가...
'''
from collections import deque
import sys

def bfs(r):
    v = [False] * (N + 1)
    v[r] = True
    cnt = 1
    dq.append(r)
    while dq:
        x = dq.popleft()
        for y in mtx[x]:
            if not v[y]:
                v[y] = True
                cnt += 1
                dq.append(y)
    return cnt

N, M = map(int, sys.stdin.readline().rstrip().split())
mtx = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    mtx[b].append(a)
dq = deque()
count = list()
max_cnt = 0
for i in range(1, N + 1):
    if mtx[i]:
        n = bfs(i)
        if max_cnt <= n:
            if max_cnt < n:
                count = list()
            max_cnt = n
            count.append(i)
print(*count)