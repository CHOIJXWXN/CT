'''
텀 프로젝트
dfs
'''
import sys

sys.setrecursionlimit(10**6)

def dfs(n):
    global cnt
    v[n] = True
    connect.append(n)
    next = pair[n]
    if v[next]:
        if next in connect:
            cnt -= connect.index(next)
            return True
        return False
    else:
        if dfs(next):
            cnt += 1
            return True
        return False

read = sys.stdin.readline
T = int(read())
for _ in range(T):
    N = int(read())
    pair = [0] + list(map(int, read().split()))
    v = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if not v[i]:
            connect = list()
            if dfs(i):
                cnt += 1
    print(N - cnt)