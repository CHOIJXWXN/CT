'''
참외밭
각 방향마다 제일 긴 것이 가로/세로 길이
제일 긴 변과 붙어 있는 변은 오목변일 수 없음
'''
N = int(input())
l = []
# 가로 길이, 세로 길이, 해당 인덱스들 저장
w, h, w_idx, h_idx = 0, 0, 0, 0
for i in range(6):
    d, length = map(int, input().split())
    if d < 3 and w < length:
        w = length
        w_idx = i
    elif d > 2 and h < length:
        h = length
        h_idx = i
    l.append(length)
# minus : 빼줘야하는 면적
minus = 1
# 오목 변이 아닌 애들 거르기
no = [w_idx - 1, w_idx, w_idx + 1, h_idx - 1 , h_idx, h_idx + 1]
for n in no:
    l[n % 6] = 1
for i in l:
    minus *= i
print(N * (w * h - minus))