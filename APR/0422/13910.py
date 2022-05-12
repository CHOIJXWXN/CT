'''
개업
'''
import sys

read = sys.stdin.readline
N, M = map(int, read().split())
W = [0] + list(map(int, read().split()))
w = set()                                               # 한 번에 요리할 수 있는 짜장면 수를 담을 셋
for i in range(M + 1):
    for j in range(i + 1, M + 1):
        if W[i] + W[j] <= N:                            # 원하는 요리양보다 작을 때만 w에 담기
            w.update([W[i] + W[j]])
d = [1 if i in w else 10**5 for i in range(N + 1)]      # dp배열 (한 번에 요리할 수 있는 짜장면 수에 1 대입, 그 외에는 INF를 대입하여 초기화)
for i in range(1, N + 1):                               # N번 반복
    for size in w:                                      # 한 번에 요리할 수 있는 짜장면 수마다 반복
        if i - size >= 0:                               # 인덱스 에러 방지
            d[i] = min(d[i], d[i - size] + 1)           # 현재 저장된 비용과 방금 계산한 비용 비교하여 최솟값 업데이트
print(d[-1]) if d[-1] < 10**5 else print(-1)            # 마지막 인덱스 즉 d[N] 출력 (여전히 INF값이라면 -1 출력)