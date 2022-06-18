"""
욕심쟁이 판다
"""
# bfs 시간 초과

# from collections import deque
#
#
# def bfs(r, c):
#     v = [[False] * N for _ in range(N)]
#     q = deque([(r, c, 1)])
#     v[r][c] = True
#     while q:
#         x, y, cnt = q.popleft()
#         for i in range(4):
#             nx, ny = x + d[i][0], y + d[i][1]
#             if 0 <= nx < N and 0 <= ny < N and not v[nx][ny] and arr[x][y] < arr[nx][ny]:
#                 q.append((nx, ny, cnt + 1))
#                 v[nx][ny] = True
#         tot_cnt = cnt
#     return tot_cnt
#
#
# import sys
# read = sys.stdin.readline
# N = int(read())
# arr = [list(map(int, read().split())) for _ in range(N)]
# d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# max_cnt = 0
# for i in range(N):
#     for j in range(N):
#         max_cnt = max(bfs(i, j), max_cnt)
# print(max_cnt)

# dfs dp (pypy 메모리 초과)

import sys
sys.setrecursionlimit(10**6)


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 1
    for dir in d:
        nr, nc = r + dir[0], c + dir[1]
        if 0 <= nr < N and 0 <= nc < N and arr[r][c] < arr[nr][nc]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    return dp[r][c]


read = sys.stdin.readline
N = int(read())
arr = [list(map(int, read().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))
print(ans)
