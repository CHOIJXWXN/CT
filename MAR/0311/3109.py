'''
빵집
'''
def dfs(r, c):
    mtx[r][c] = 'o'
    # 오른쪽 끝까지 도착했을 때 cnt + 1
    if c == C - 1:
        global cnt
        cnt += 1
        return True
    # 오른쪽 위 이동
    if r > 0 and mtx[r - 1][c + 1] == '.':
        if dfs(r - 1, c + 1):
            return True
    # 오른쪽 이동
    if mtx[r][c + 1] == '.':
        if dfs(r, c + 1):
            return True
    # 오른쪽 아래 이동
    if r < R - 1 and mtx[r + 1][c + 1] == '.':
        if dfs(r + 1, c + 1):
            return True
    # 어디도 이동할 수 없다면 False
    return False

R, C = map(int, input().split())
mtx = [list() for _ in range(R)]
for i in range(R):
    mtx[i].extend(input())
cnt = 0
for i in range(R):
    dfs(i, 0)
print(cnt)