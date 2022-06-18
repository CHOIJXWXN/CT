"""
감시
"""
import sys


def dfs(cnt, mtx):
    global min_zero
    if cnt == cctvs:
        zero = 0
        for i in range(R):
            zero += mtx[i].count(0)
        min_zero = min(zero, min_zero)
        return
    temp = [mtx[i][:] for i in range(R)]
    typ, rr, cc = cctv[cnt]
    for direction in d[typ]:
        for dire in direction:
            nr, nc = rr, cc
            while True:
                nr += dire[0]
                nc += dire[1]
                if not (0 <= nr < R and 0 <= nc < C):
                    break
                if temp[nr][nc] == 6:
                    break
                elif temp[nr][nc] == 0:
                    temp[nr][nc] = -1
        dfs(cnt + 1, temp)
        temp = [mtx[i][:] for i in range(R)]


read = sys.stdin.readline
R, C = map(int, read().split())
arr = [[0] * C for _ in range(R)]
cctv = list()
d = [[],
     [[[-1, 0]], [[1, 0]], [[0, -1]], [[0, 1]]],
     [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]],
     [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]],
     [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]]],
     [[[1, 0], [-1, 0], [0, 1], [0, -1]]]]
for r in range(R):
    arr[r] = list(map(int, read().split()))
    for c in range(C):
        if 0 < arr[r][c] < 6:
            cctv.append((arr[r][c], r, c))    # 유형, 행, 열
cctvs = len(cctv)
min_zero = R * C
dfs(0, arr)
print(min_zero)
