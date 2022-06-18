'''
상범 빌딩
bfs
'''
from collections import deque
import sys

read = sys.stdin.readline
D = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
while True:
    L, R, C = map(int, read().split())  # 층 행 열
    if not (L or R or C):
        break
    B = [list() for _ in range(L)]
    V = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    S, E = list(), list()
    for i in range(L):
        for j in range(R):
            B[i].append(read()) # 개행 포함되어 있음
            if not S:
                for k in range(C):
                    if B[i][j][k] == 'S':
                        S = [i, j, k]
            if not E:
                for k in range(C):
                    if B[i][j][k] == 'E':
                        E = [i, j, k]
        read()
    q = deque()
    q.append(S)
    V[S[0]][S[1]][S[2]] = 0
    msg = 'Trapped!'
    while q:
        x = q.popleft()
        idx = V[x[0]][x[1]][x[2]]
        if x[0] == E[0] and x[1] == E[1] and x[2] == E[2]:
            msg = 'Escaped in ' + str(idx) + ' minute(s).'
            break
        for d in D:
            nx = x[0] + d[0]
            ny = x[1] + d[1]
            nz = x[2] + d[2]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and V[nx][ny][nz] < 0 and B[nx][ny][nz] != '#':
                V[nx][ny][nz] = idx + 1
                q.append([nx, ny, nz])
    print(msg)