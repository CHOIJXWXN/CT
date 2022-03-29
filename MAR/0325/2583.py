'''
영역 나누기
'''
import sys
sys.setrecursionlimit(10**6)
def dfs(r, c):
    cnt = 1
    mtx[r][c] = 0
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < M and 0 <= nc < N and mtx[nr][nc]:
            cnt += dfs(nr, nc)
    return cnt

M, N, K = map(int, sys.stdin.readline().rstrip().split())
mtx = [[1] * N for _ in range(M)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
group = 0
count = list()
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            mtx[j][i] = 0
for i in range(M):
    for j in range(N):
        if mtx[i][j]:
            group += 1
            count.append(dfs(i, j))
print(group)
print(*sorted(count))