'''
숫자 카드
'''
import sys

read = sys.stdin.readline

N = int(read())
have = list(map(int, read().rstrip().split()))
M = int(read())
want = list(map(int, read().split()))
ans = {want[i]: 0 for i in range(M)}
for i in range(N):
    if have[i] in ans.keys():
        ans[have[i]] = 1
print(*ans.values())