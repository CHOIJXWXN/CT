'''
부분수열의 합
'''
import sys

read = sys.stdin.readline
N = int(read())
S = sorted(list(map(int, read().split())))
ans = 0
for s in S:
    if ans + 1 < s:
        break
    ans += s
print(ans + 1)

'''
S = [1, 2, 3, 4, 5]
1, 2, 3, 4, 5, ..., 15

S = [1, 2, 4, 9]
1, 2, 3, 4, 5, 6, 7
'''