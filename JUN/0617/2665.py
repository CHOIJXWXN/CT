"""
미로만들기
pypy가 더 많이 나옴 이거 나중에 정리 한 번 해보면 좋을 듯
그냥저냥 다익스트라
"""
import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
mtx = [list() for _ in range(N)]
black = [[2500] * N for _ in range(N)]          # 비용 저장할 리스트 (검은 방에 가면 비용 1이 든다)
for i in range(N):
    mtx[i] = list(map(int, read().rstrip()))
D = [[1, 0], [0, 1], [-1, 0], [0, -1]]          # 사방탐색 델타배열
q = deque([(0, 0)])                             # bfs를 위한 큐 (시작점이 0, 0)
black[0][0] = 0                                 # 시작점은 언제나 흰 방
while q:
    x, y = q.popleft()                          # 큐에 있는 좌표 하나 뽑아서 네 방향 돌려주고
    for d in D:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < N:         # 범위 안에 있는지 확인
            if black[nx][ny] > black[x][y] + (not mtx[nx][ny]):     # 옮겨갈 좌표의 비용이 (현재 좌표의 비용 + 옮겨갈 때의 비용) 보다 크면
                black[nx][ny] = black[x][y] + (not mtx[nx][ny])     # 옮겨갈 좌표의 비용 바꿔줌 (더 낮아지도록)
                q.append((nx, ny))
print(black[-1][-1])
