'''
'나교수' 교수님의 악필
받은 문자열에서 0과 6을 9로 바꾸어 평균 구하기
'''
N = int(input())                        # 학생 수 입력값 저장
tot = 0                                 # 총 점수 변수
for i in range(N):                      # 학생마다 반복
    score = input()                     # 학생 점수 입력값 저장
    score = score.replace('0', '9')     # 0을 9로 바꿈
    score = score.replace('6', '9')     # 6을 9로 바꿈
    if int(score) > 100:                # 100이 넘으면
        score = '100'                   # 100으로 바꿈
    tot += int(score)                   # 총 점수에 더하기

# round가 잘 안 먹어서 직접 구현한 것
q = tot // N
if tot % N < N / 2:                    
    print(q)
else:
    print(q + 1)