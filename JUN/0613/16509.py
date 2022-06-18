"""
장군
"""
from collections import deque

X, Y = map(int, input().split())    # 상
R, C = map(int, input().split())    # 왕
v = [[False] * 9 for _ in range(10)]
D = [[[-1, 0], [-2, -1], [-3, -2]], [[-1, 0], [-2, 1], [-3, 2]],    # 상
     [[0, 1], [-1, 2], [-2, 3]], [[0, 1], [1, 2], [2, 3]],          # 우
     [[1, 0], [2, -1], [3, -2]], [[1, 0], [2, 1], [3, 2]],          # 하
     [[0, -1], [-1, -2], [-2, -3]], [[0, -1], [1, -2], [2, -3]]]    # 좌
q = deque([[X, Y, 0]])
v[X][Y] = True
ans = -1
while q:
    n = q.popleft()
    if n[0] == R and n[1] == C:
        ans = n[2]
        break
    for dir in D:
        flag = True
        for d in range(3):
            nx, ny = n[0] + dir[d][0], n[1] + dir[d][1]
            if (d < 2 and nx == R and ny == C) or not (0 <= nx < 10 and 0 <= ny < 9):
                flag = False
                break
        nx, ny = n[0] + dir[-1][0], n[1] + dir[-1][1]
        if flag and not v[nx][ny]:
            q.append([nx, ny, n[2] + 1])
            v[nx][ny] = True
print(ans)