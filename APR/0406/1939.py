'''
중량제한
'''
# 플로이드 와샬
# import sys

# read = sys.stdin.readline
# N, M = map(int, read().rstrip().split())
# d = [[-10**15] * (N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     A, B, W = map(int, read().rstrip().split())
#     d[A][B] = W
#     d[B][A] = W
# I, F = map(int, read().rstrip().split())
# for l in range(1, N + 1):
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             d[i][j] = max(max(d[i][l], d[l][j]), d[i][j])
# print(d[I][F])

from collections import deque
import sys

def isOK(w):
    v[I] = True
    q = deque([I])
    while q:
        now = q.popleft()
        if now == F:
            return True
        for next, W in mtx[now]:
            if not v[next] and w <= W:
                q.append(next)
                v[next] = True
    return False

read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
mtx = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B, W = map(int, read().rstrip().split())
    mtx[A].append([B, W])
    mtx[B].append([A, W])
I, F = map(int, read().rstrip().split())
b, t = 0, 10**9
while b <= t:
    v = [False] * (N + 1)
    m = (b + t) // 2
    if isOK(m):
        b = m + 1
    else:
        t = m - 1
print(t)