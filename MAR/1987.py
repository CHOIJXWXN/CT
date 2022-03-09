'''
알파벳
(1, 1)에서 말이 움직여서 알파벳이 다른 곳으로 움직일 때 가장 많이 움직일 수 있는 칸 수
'''

def dfs(r, c, cnt, max_cnt):                # 인자로 행, 열, 현재 몇 칸째인지, 최대 몇 칸까지 가봤는지
    max_cnt = max(max_cnt, cnt)             # 최대 칸수 업데이트
    alphs[ord(mtx[r][c]) - ord('A')] = 1    # 지금 옮겨간 행 열에 위치하는 알파벳 개수 = 1
    for i in range(4):                      # 상하좌우 반복
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < R and 0 <= nc < C and not alphs[ord(mtx[nr][nc]) - ord('A')]:  # 옮긴 좌표가 틀 안에 있고 아직 만나본 적 없는 알파벳일 때
            max_cnt = max(dfs(nr, nc, cnt + 1, max_cnt), max_cnt)                   # 최대 칸수 업데이트
    alphs[ord(mtx[r][c]) - ord('A')] = 0    # 다시 알파벳 개수 = 0 (방문하지 않았을 때로 바꿈)
    return max_cnt                          # 최대 칸수 반환

R, C = map(int, input().split())
alphs = [0] * 26                            # 알파벳 개수 (0이면 없음 1이면 있음)
mtx = []
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]      # 인접 상하좌우
for i in range(R):
    mtx.append(input())
print(dfs(0, 0, 1, 0))                      # 0, 0에서 시작 (첫 칸도 카운트하므로 1)