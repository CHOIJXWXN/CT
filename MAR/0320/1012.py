'''
유기농 배추
배추가 심겨져있는 좌표를 입력값으로 받음
'''
from collections import deque
import sys

def bfs(r, c):
    dq.append((r, c))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < M and 0 <= ny < N and [nx, ny] in C and not v[C.index([nx, ny])]:
                dq.append((nx, ny))
                v[C.index([nx, ny])] = True

T = int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    v = [False] * K
    cnt = 0
    C = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]
    dq = deque()
    for i in range(K):
        if not v[i]:
            bfs(C[i][0], C[i][1])
            cnt += 1
    print(cnt)