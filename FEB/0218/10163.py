'''
색종이
'''
# 직접 카운트하는 방법
# N = int(input())
# white = [[0] * 1001 for i in range(1001)]
# count = [0] * N
# for i in range(N):
#     x, y, w, h = map(int, input().split())
#     for j in range(w):
#         for k in range(h):
#             if white[x + j][y + k]:
#                 count[white[x + j][y + k] - 1] -= 1
#             white[x + j][y + k] = i + 1
#             count[i] += 1
# print(*count, sep='\n')

# 내장함수 사용하는 방법
# N = int(input())
# white = [[0] * 1001 for i in range(1001)]
# for i in range(N):
#     x, y, w, h = map(int, input().split())
#     for j in range(w):
#         for k in range(h):
#             white[x + j][y + k] = i + 1
# for i in range(N):
#     cnt = 0
#     for j in range(1001):
#         cnt += white[j].count(i + 1)
#     print(cnt)

# 구글링 결과
# 2중 for문을 사용하지 않도록 하는 것이 포인트
N = int(input())
white = [[0] * 1001 for i in range(1001)]
for i in range(N):
    x, y, w, h = map(int, input().split())
    for j in range(w):
        white[x + j][y:y + h] = [i + 1] * h
for i in range(N):
    cnt = 0
    for j in range(1001):
        cnt += white[j].count(i + 1)
    print(cnt)