'''
단지번호붙이기
야옹님이 알려주신 연결요소 크기 방법 사용
'''
def dfs(r, c):
    count = 1
    visited[r][c] = True
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < N and (not visited[nr][nc]) and mtx[nr][nc] == '1':
            count += dfs(nr, nc)
    return count

N = int(input())
mtx = [list() for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
group = 0
cnt = list()
for i in range(N):
    mtx[i] = input()
    
for i in range(N):
    for j in range(N):
        if mtx[i][j] == '1' and not visited[i][j]:
            cnt.append(dfs(i, j))
            group += 1
            
print(group)
print(*sorted(cnt), sep='\n')