'''
피리 부는 사나이
'''
def dfs(r, c, idx):
    visited[r][c] = idx
    nr, nc = r, c
    if mtx[r][c] == 'D':
        nr += 1
    elif mtx[r][c] == 'U':
        nr -= 1
    elif mtx[r][c] == 'R':
        nc += 1
    elif mtx[r][c] == 'L':
        nc -= 1
    if 0 <= nr < N and 0 <= nc < M:
        if visited[nr][nc]:
            if visited[nr][nc] != idx:
                visited[r][c] = visited[nr][nc]
                return False
        else:
            if not dfs(nr, nc, idx):
                visited[r][c] = visited[nr][nc]
                return False
    return True

N, M = map(int, input().split())
mtx = list()
for _ in range(N):
    mtx.append(input())
visited = [[0] * M for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and dfs(i, j, cnt):
            cnt += 1
print(cnt - 1)