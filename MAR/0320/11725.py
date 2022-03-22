'''
트리의 부모 찾기
'''
import sys

sys.setrecursionlimit(10**6)

def delete(r):
    for child in tree[r]:
        p[child] = r
        tree[child].remove(r)
        delete(child)

N = int(input())
tree = [list() for _ in range(N + 1)]
p = [0] * (N + 1)
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    tree[x].append(y)
    tree[y].append(x)
delete(1)
print(*p[2:], sep='\n')