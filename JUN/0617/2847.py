"""
게임을 만든 동준이
(?)
"""
import sys
read = sys.stdin.readline

N = int(read())                     # 레벨 수 입력값
cnt, num = 0, list()                # 출력할 값 / 입력 받을 점수 리스트 초기화
for _ in range(N):
    num.append(int(read()))
for i in range(N - 1, 0, -1):       # N - 1 ~ 1 반복
    d = num[i] - num[i - 1]         # 레벨 간 점수차
    if d < 1:                       # 1보다 작으면 (아래 레벨의 점수가 위 레벨의 점수보다 크거나 같으면)
        cnt += - d + 1
        num[i - 1] = num[i] - 1     # 아래 레벨 점수 내려주기 (내려준 만큼 cnt에 더해주기)
print(cnt)
