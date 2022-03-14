'''
빵집
'''
def dfs(r, c):
    mtx[r][c] = 'o'
    if c == C - 1:
        global cnt
        cnt += 1
        return True
    if r > 0 and mtx[r - 1][c + 1] == '.':
        if dfs(r - 1, c + 1):
            return True
    if mtx[r][c + 1] == '.':
        if dfs(r, c + 1):
            return True
    if r < R - 1 and mtx[r + 1][c + 1] == '.':
        if dfs(r + 1, c + 1):
            return True
    return False

R, C = map(int, input().split())
mtx = [list() for _ in range(R)]
for i in range(R):
    mtx[i].extend(input())
cnt = 0
for i in range(R):
    dfs(i, 0)
print(cnt)