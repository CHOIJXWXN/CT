"""
수 고르기
얘가 왜 골드지? 느낌
"""
import sys
read = sys.stdin.readline

N, M = map(int, read().split())         # 입력
arr = list()
for _ in range(N):
    arr.append(int(read()))
arr.sort()                              # 오름차순 정렬
s, e, d = 0, 1, 2_000_000_001           # start idx, end idx, 두 값의 차이 초기화
while s < N and e < N:                  # 두 인덱스가 범위를 벗어나지 않을 때까지
    if arr[e] - arr[s] >= M:            # 차가 M 이상일 때
        d = min(d, arr[e] - arr[s])     # 차의 최솟값을 d에 저장
        s += 1                          # 차가 더 작아졌으면 하기 때문에 s 오른쪽으로 이동
    else:                               # 차가 M보다 작으면
        e += 1                          # 차가 더 커졌으면 하기 때문에 e 오른쪽으로 이동
print(d)
