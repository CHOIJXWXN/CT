"""
승부 조작
"""
# 시간 초과

# import sys
#
#
# def find(r, c):
#     global max_cnt
#     for i in range(1, 5):
#         nr, nc, nnr, nnc, cnt = r, c, r, c, 1
#         while True:
#             nr += d[i][0]
#             nc += d[i][1]
#             if not (0 <= nr < N and 0 <= nc < N):
#                 break
#             if arr[nr][nc] == 1:
#                 cnt += 1
#         while True:
#             nnr -= d[i][0]
#             nnc -= d[i][1]
#             if not (0 <= nnr < N and 0 <= nnc < N):
#                 break
#             if arr[nnr][nnc] == 1:
#                 cnt += 1
#         max_cnt = max(max_cnt, cnt)
#
#
# read = sys.stdin.readline
# N = int(read())
# arr = [[0] * N for _ in range(N)]
# whites = list()
# d = [[0, 0], [1, 0], [0, 1], [1, 1], [1, -1]] # 더미 / 하 / 우 / 대각선1 / 대각선2
# max_cnt = 0
# for i in range(N):
#     arr[i] = list(map(int, read().split()))
#     for j in range(N):
#         if arr[i][j] == 1:
#             find(i, j)
#         if arr[i][j] == 2:
#             whites.append((i, j))
# for white in whites:
#     find(*white)
# print(max_cnt)

# dp

import sys


def add(r, c, dp, d):
    if arr[r][c] == 1:
        for di in range(4):
            if not dp[di][r][c]:
                dp[di][r][c] = 1
            if 0 <= r + d[di][0] < N and 0 <= c + d[di][1] < N:
                dp[di][r][c] = dp[di][r + d[di][0]][c + d[di][1]] + 1


read = sys.stdin.readline
N = int(read())
arr = [list(map(int, read().split())) for _ in range(N)]
dp1 = [[[0] * N for _ in range(N)] for _ in range(4)]   # 하 / 우 / 하우 / 하좌
dp2 = [[[0] * N for _ in range(N)] for _ in range(4)]   # 상 / 좌 / 상좌 / 상우
d1 = [[-1, 0], [0, -1], [-1, -1], [-1, 1]]
d2 = [[1, 0], [0, 1], [1, 1], [1, -1]]
for i in range(N):
    for j in range(N):
        add(i, j, dp1, d1)
for i in range(N):
    for j in range(N):
        add(N - 1 - i, N - 1 - j, dp2, d2)
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(4):
            ans = max(ans, dp1[k][i][j])
            if arr[i][j] == 2:
                if not (0 <= i + d1[k][0] < N and 0 <= j + d1[k][1] < N) and not (0 <= i + d2[k][0] < N and 0 <= j + d2[k][1] < N):
                    ans = max(ans, 1)
                elif not (0 <= i + d1[k][0] < N and 0 <= j + d1[k][1] < N):
                    ans = max(ans, dp2[k][i + d2[k][0]][j + d2[k][1]] + 1)
                elif not (0 <= i + d2[k][0] < N and 0 <= j + d2[k][1] < N):
                    ans = max(ans, dp1[k][i + d1[k][0]][j + d1[k][1]] + 1)
                else:
                    ans = max(ans, dp1[k][i + d1[k][0]][j + d1[k][1]] + dp2[k][i + d2[k][0]][j + d2[k][1]] + 1)
print(ans)


