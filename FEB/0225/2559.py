'''
수열
N개 중 K개의 연속된 수를 더했을 때 최댓값
'''
N, K = map(int, input().split())
temp = list(map(int, input().split()))
sum = 0
# 일단 0부터 K-1까지 더한 값 저장
for i in range(K):
    sum += temp[i]
# rs : 출력할 값
rs = sum
'''
0  1  2  3  4  5  6  7  8  9
3 -2 -4 -9  0  3  7 13  8 -3
sum = 3 + (-2) + (-4) + (-9) + 0
다시 업데이트
sum - 3 + 3
다시 업데이트
sum -(-2) + 7
다시 업데이트
sum -(-4) + 13
...
'''
for i in range(N - K):
    sum += temp[i + K] - temp[i]
    rs = max(rs, sum)
print(rs)