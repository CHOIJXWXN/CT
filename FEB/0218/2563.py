'''
색종이
'''
white = [[0] * 100 for i in range(100)]     # 하얀 도화지 행렬
tot = 0                                     # 넓이 변수
N = int(input())                            # 색종이 개수 입력값 저장
for i in range(N):                          # 모든 색종이 반복
    x, y = map(int, input().split())        # 왼쪽 아래 꼭짓점 좌표 저장
    for j in range(10):                     # 10번 반복
        for k in range(10):                 # 10번 반복
            white[x + j][y + k] = 1         # x ~ x + 9 와 y ~ y + 9 모두 1로 변환
for i in white:                             # 하얀 도화지에서 
    tot += sum(i)                           # 모든 수를 더하면
print(tot)                                  # 넓이 출력