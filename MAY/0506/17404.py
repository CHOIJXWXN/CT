'''
RGB거리 2
dp
'''
import sys

read = sys.stdin.readline
N = int(read())
cost = list()
for _ in range(N):
    cost.append(list(map(int, read().split())))
minD = 10**6                                # 최소비용
for i in range(3):                          # 첫번째 집이 R, G, B일 때 반복
    d = [[10**6] * 3 for _ in range(N)]     # d[i][j] = i번째 집이 j색을 선택했을 때 가장 적은 비용
    d[0][i] = cost[0][i]
    for j in range(1, N):
        for idx in range(3):
            d[j][idx] = min(d[j - 1][(idx + 1) % 3], d[j - 1][(idx + 2) % 3]) + cost[j][idx]
    minD = min(minD, d[N - 1][(i + 1) % 3], d[N - 1][(i + 2) % 3])
print(minD)