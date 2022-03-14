import sys
sys.setrecursionlimit(1000000)

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(x,y,h):
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and arr[nx][ny] > h:
            arr[nx][ny] = True
            dfs(nx, ny, h)
    
result = 0
for t in range(10):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > t and visited[i][j] == False:
                cnt += 1
                visited[i][j] = True
                dfs(i,j,t)
    if result < cnt:
        result = cnt

print(result)