'''
안전 영역
비올 때 잠기지 않는 지역의 개수
'''
import sys
sys.setrecursionlimit(10**6)

def dfs(r, c, H):
    visited[r][c] = True
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < N and (not visited[nr][nc]) and mtx[nr][nc] > H:   # 인접좌표가 틀 안에 있고, 아직 방문하지 않았으면서, 높이 H보다 클 때
            dfs(nr, nc, H)

N = int(input())
mtx = [list() for _ in range(N)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 인접 상하좌우
max_group = 0
cnt = list()
heights = set()
for i in range(N):
    mtx[i] = list(map(int, sys.stdin.readline().rstrip().split()))  # 입력값 저장
    heights.update(mtx[i])                                          # 높이 중복 없이 저장

for k in heights:                                                   # 해당 높이마다 반복

    visited = [[False for _ in range(N)] for _ in range(N)]         # 방문 리스트
    group = 0                                                       # 아직 0개 지역
    for i in range(N):                                              # mtx 반복
        for j in range(N):
            if mtx[i][j] > k and not visited[i][j]:                 # 해당 높이보다 높고 아직 방문 안 한 지역
                dfs(i, j, k)                                        # dfs
                group += 1                                          # 지역 개수 + 1
    
    max_group = max_group if max_group > group else group           # 높이에 따른 지역 개수 중 제일 많은 수 저장

print(max_group) if max_group else print(1)