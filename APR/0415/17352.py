'''
여러분의 다리가 되어 드리겠습니다!
'''
# dfs 연결요소
# import sys

# sys.setrecursionlimit(10**6)

# def dfs(r):
#     v[r] = True
#     for c in mtx[r]:
#         if not v[c]:
#             dfs(c)

# read = sys.stdin.readline
# N = int(read())
# mtx = [list() for _ in range(N + 1)]
# v = [False] * (N + 1)
# for _ in range(N - 2):
#     a, b = map(int, read().rstrip().split())
#     mtx[a].append(b)
#     mtx[b].append(a)

# dfs(1)

# for i in range(2, N + 1):
#     if not v[i]:
#         print(1, i)
#         break

# 유니온 파인드
import sys

def union(a, b):
    a, b = find(a), find(b)
    idx[max(a, b)] = min(a, b)

def find(a):
    if a == idx[a]:
        return a
    idx[a] = find(idx[a])
    return idx[a]

read = sys.stdin.readline
N = int(read())
idx = [i for i in range(N + 1)]
for _ in range(N - 2):
    a, b = map(int, read().rstrip().split())
    union(a, b)
for i in range(2, N + 1):
    if find(1) != find(i):
        print(1, i)
        break