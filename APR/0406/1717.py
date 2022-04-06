'''
집합의 표현
'''
import sys
sys.setrecursionlimit(10**6)
def union(a, b):
    a = find(a)
    b = find(b)
    if (a == b):
        return
    if a < b:
        idx[b] = a
    else:
        idx[a] = b

def find(a):
    if a == idx[a]:
        return a
    p = find(idx[a])
    idx[a] = p
    return idx[a]

n, m = map(int, input().split())
idx = [i for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().rstrip().split())
    if op == 0:
        union(a, b)
    else:
        print("YES") if find(a) == find(b) else print("NO")