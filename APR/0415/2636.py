'''
치즈
'''
import sys

sys.setrecursionlimit(10**6)

def dfs(r, c):
    global cnt
    for dir in d:
        nr = r + dir[0]
        nc = c + dir[1]
        if 0 <= nr < R and 0 <= nc < C and not v[nr][nc]:
            v[nr][nc] = True
            if mtx[nr][nc] == 1:
                cnt -= 1
                mtx[nr][nc] = 0
            else:
                dfs(nr, nc)

R, C = map(int, sys.stdin.readline().rstrip().split())
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
time, cnt, last = 0, 0, 0
mtx = list()
for r in range(R):
    mtx.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for c in range(C):
        cnt += mtx[r][c]
while cnt > 0:
    v = [[False for _ in range(C)] for _ in range(R)]
    time += 1
    last = cnt
    dfs(0, 0)

print(time, last, sep='\n')