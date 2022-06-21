"""
행렬 곱셈 순서
dp
"""
import sys
read = sys.stdin.readline

N = int(read())
mtx = [list() for _ in range(N)]
dp = [[0] * N for _ in range(N)]                # dp[A][B] = A부터 B까지 곱했을 때 최소 연산 수
for i in range(N):
    mtx[i] = list(map(int, read().split()))
# 행과 열의 차이
for i in range(1, N):
    # j번째 행
    for j in range(N - i):
        if i == 1:
            dp[j][j + i] = mtx[j][0] * mtx[j][1] * mtx[j + i][1]
            continue
        dp[j][j + i] = 2**32
        # 중간에 거치는 곳
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + mtx[j][0] * mtx[k][1] * mtx[j + i][1])
print(dp[0][-1])
"""
   A  B  C  D  E
A  0 AB ABC
B     0 BC 
C        0 CD 
D           0 DE
E              0
"""