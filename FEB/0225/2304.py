'''
창고 다각형
1. 제일 긴 막대가 나올 때까지, 자기보다 오른쪽 막대가 더 높으면 면적 계산, 더 짧으면 막대 치우기
2. 방향만 반대
3. 제일 긴 막대들끼리 차지하는 면적 계산
'''
N = int(input())
columns = []
height, tot = 0, 0
for i in range(N):
    x, y = map(int, input().split())
    columns.append([x, y])
    # 최대 길이
    height = y if height < y else height
# x좌표 순으로 정렬
columns.sort(key = lambda x : x[0])
# 왼쪽 출발
while columns[0][1] < height:
    if columns[1][1] > columns[0][1]:
        tot += columns[0][1] * (columns[1][0] - columns[0][0])
        columns.pop(0)
    else:
        columns.pop(1)
# 오른쪽 출발
while columns[-1][1] < height:
    if columns[-2][1] > columns[-1][1]:
        tot += columns[-1][1] * (columns[-1][0] - columns[-2][0])
        columns.pop()
    else:
        columns.pop(-2)
# 제일 긴 막대 면적 더하기
tot += height * (columns[-1][0] - columns[0][0] + 1)
print(tot)