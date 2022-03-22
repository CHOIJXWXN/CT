'''
섬의 개수
'''
from collections import deque
import sys

def bfs(r, c):
    mtx[r][c] = 0
    dq = deque()
    dq.append((r, c))
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < h and 0 <= ny < w and mtx[nx][ny]:
                dq.append((nx, ny))
                mtx[nx][ny] = 0

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    cnt = 0
    mtx = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if mtx[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)