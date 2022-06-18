'''
인사성 밝은 곰곰이
희한하게 pypy가 더 느림(?)
'''
import sys

read = sys.stdin.readline
N = int(read())
M = dict()
ans = 0
for _ in range(N):
    new = read()
    if new == 'ENTER\n':
        ans += len(M)
        M = dict()
    else:
        M[new] = 1
print(ans + len(M))