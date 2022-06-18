"""
공유기 설치

사이의 거리가 D보다 크거나 같은 집을 선택했을 때 그 개수가 C보다 크거나 같으면 D를 늘림 / C보다 작으면 D를 줄임 (이분탐색)
C = 3
a b c d e f g
 3 4 5 2 6 1
D = 4
a -> c -> d -> f 총 4개
D = 8
a -> d -> f      총 3개
D = 10
a -> d           총 2개
"""
import sys
read = sys.stdin.readline

N, C = map(int, read().split())
X = list()
for _ in range(N):
    X.append(int(read()))
X.sort()
b, t = 0, X[-1] - X[0]
while b <= t:
    m = (b + t) // 2
    prev, cnt = 0, 1
    for i in range(N):
        if X[i] - X[prev] >= m:
            cnt += 1
            prev = i
    if cnt >= C:
        b = m + 1
    else:
        t = m - 1
print(t)
