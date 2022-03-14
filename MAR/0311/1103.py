'''
게임
'''
import sys
sys.setrecursionlimit(10**6)

def dfs(r, c, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    n = int(mtx[r][c])
    d = [[n, 0], [-n, 0], [0, n], [0, -n]]
    for i in range(4):
        if max_cnt == -1:
            return
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < M and mtx[nr][nc] != 'H' and cnt + 1 > dp[nr][nc]:
            if mtx[nr][nc] == 'V':
                print(-1)
                exit()
            dp[nr][nc] = cnt + 1
            mtx[r][c] = 'V'
            dfs(nr, nc, cnt + 1)
            mtx[r][c] = str(n)

N, M = map(int, input().split())
mtx = [list() for _ in range(N)]
for i in range(N):
    mtx[i].extend(input())
dp = [[0] * M for _ in range(N)]
max_cnt = 1
dfs(0, 0, 1)
print(max_cnt)