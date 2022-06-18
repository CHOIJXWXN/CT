'''
돌다리 건너기
'''
import sys
 
read = lambda: sys.stdin.readline().rstrip()
M = read()
D = read()
A = read()
lenM, lenD = len(M), len(D)
dp = [[[0] * 2 for _ in range(lenM)] for _ in range(lenD)]
for i in range(lenD):
    dp[i][0][0] = (D[i] == M[0])
    dp[i][0][1] = (A[i] == M[0])
for i in range(lenD):
    for j in range(1, lenM):
        if D[i] == M[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j - 1][1] 
        if A[i] == M[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j - 1][0]
ans = 0
for i in range(lenD):
    ans += (dp[i][-1][0] + dp[i][-1][1])
print(ans)