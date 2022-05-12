'''
내리막길
'''
import sys
sys.setrecursionlimit(10**6)
def dfs(r, c):
    if r == R - 1 and c == C - 1:
        return 1
    dp[r][c] = 0
    for D in d:
        nr = r + D[0]
        nc = c + D[1]
        if 0 <= nr < R and 0 <= nc < C and mtx[nr][nc] < mtx[r][c]:
            dp[r][c] += dfs(nr, nc)
    return dp[r][c]

read = sys.stdin.readline
R, C = map(int, read().split())
mtx = [list(map(int, read().split())) for _ in range(R)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dp = [[0] * C for _ in range(R)]
dfs(0, 0)
print(dp[0][0])