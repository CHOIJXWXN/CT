'''
바이러스
'''
def dfs(n):
    visited[n] = True
    for child in con[n]:
        if not visited[child]:
            dfs(child)

N = int(input())
n = int(input())
con = [list() for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(n):
    com1, com2 = map(int, input().split())
    con[com1].append(com2)
    con[com2].append(com1)
dfs(1)
print(visited.count(True) - 1)