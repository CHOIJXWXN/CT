'''
미로 탐색
0 : X    1 : O
1, 1  ->  N, M  최소 칸 수

7 7

1011111
1110001
1000001
1000001
1000001
1000001
1111111

'''
from collections import deque
import sys

def bfs(r, c):
    dq.append((r, c))
    while dq:
        x, y = dq.popleft()
        if (x, y) == (N - 1, M - 1):
            print(cnt[x][y])
            return
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M and mtx[nx][ny] == '1' and cnt[nx][ny] == 0:
                dq.append((nx, ny))
                cnt[nx][ny] = cnt[x][y] + 1

N, M = map(int, sys.stdin.readline().rstrip().split())
cnt = [[0] * M for _ in range(N)]
cnt[0][0] = 1
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
mtx = [sys.stdin.readline().rstrip() for _ in range(N)]
dq = deque()
bfs(0, 0)