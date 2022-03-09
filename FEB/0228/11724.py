'''
연결 요소의 개수
'''
def dfs(n):
    visited[n] = True
    for child in mtx[n]:
        if not visited[child]:
            dfs(child)
N, M = map(int, input().split())
mtx = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
group = 0
for i in range(M):
    u, v = map(int, input().split())
    mtx[u].append(v)
    mtx[v].append(u)
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        group += 1
print(group)
