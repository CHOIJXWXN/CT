'''
트리의 지름
'''
import sys
sys.setrecursionlimit(10**6)
def dfs(root):
    global max_weight, max_weight_idx
    v[root] = True
    for child in mtx[root]:
        if not v[child[0]]:
            weight[child[0]] = child[1] + weight[root]
            if weight[child[0]] >= max_weight:
                max_weight = weight[child[0]]
                max_weight_idx = child[0]
            dfs(child[0])

n = int(sys.stdin.readline().rstrip())
mtx = [list() for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().rstrip().split())
    mtx[p].append([c, w])
    mtx[c].append([p, w])
weight = [0] * (n + 1)
v = [False] * (n + 1)
max_weight, max_weight_idx = 0, 0
dfs(1)
weight = [0] * (n + 1)
v = [False] * (n + 1)
dfs(max_weight_idx)
print(max_weight)