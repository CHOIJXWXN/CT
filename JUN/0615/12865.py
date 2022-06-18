"""
평범한 배낭
"""
import sys
read = sys.stdin.readline

N, K = map(int, read().split())                     # 물품수 / 최대무게
wv = [[0] * 2 for _ in range(N + 1)]                # N개의 무게와 가치를 저장할 리스트
for i in range(1, N + 1):
    wv[i][0], wv[i][1] = map(int, read().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]          # N개의 물품당 K 무게보다 작거나 같을 때 최대 가치 합을 저장할 리스트
for n in range(1, N + 1):
    for k in range(1, K + 1):
        if wv[n][0] > k:                            # 현재 물품의 무게가 K보다 크면
            dp[n][k] = dp[n - 1][k]                 # 이전 물품까지의 가치합 저장
        else:                                       # 현재 물품의 무게가 K보다 작으면 이전 물품에서 현재 물품을 더한 가치와 이전 물품의 가치 중 큰 것을 대입
            dp[n][k] = max(dp[n - 1][k - wv[n][0]] + wv[n][1], dp[n - 1][k])
print(dp[N][K])
