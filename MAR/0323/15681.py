'''
트리와 쿼리
'''
import sys

sys.setrecursionlimit(10**6)

def sub(r):
    size[r] = 1
    for child in tree[r]:
        if not size[child]:
            sub(child)
            size[r] += size[child]

N, R, Q = map(int, sys.stdin.readline().split())
tree = [list() for _ in range(N + 1)]
size = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
sub(R)
for _ in range(Q):
    print(size[int(sys.stdin.readline())])