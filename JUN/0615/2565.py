"""
전깃줄

전봇대 A를 기준으로 계속 증가하는 최장 부분 수열 (LIS)
12015 14003 참고
"""
import sys
read = sys.stdin.readline

N = int(read())                         # 전깃줄 개수 입력
con = [-1] * 501                        # 연결 리스트 초기화
for _ in range(N):
    A, B = map(int, read().split())     # A와 B 연결
    con[A] = B                          # 리스트에 저장
d = [0]                                 # 최장 부분 수열이 저장될 리스트
for c in con:                           # 모든 연결에서 반복
    if c == -1:                         # -1이면 연결이 안된 부분이므로 패스
        continue
    if d[-1] < c:                       # 현재 저장된 수열의 가장 큰 값보다 더 큰 값이 나오면 추가
        d.append(c)
    else:                               # 그렇지 않으면 이분탐색으로 c보다 큰 값 중 가장 c와 가까운 값이 있는 곳에 c 대입
        b, t = 0, len(d)
        while b < t:
            m = (b + t) // 2
            if d[m] < c:
                b = m + 1
            else:
                t = m
        d[t] = c
print(N - len(d) + 1)                   # d 리스트에는 초기에 저장한 0도 포함되어 있으므로 +1
