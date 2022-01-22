'''
평균은 넘겠지
입력값 받아와서
점수를 다 더하고 학생 수로 나누어 평균 도출
학생의 각 점수와 평균과 대소 비교 후
학생 점수가 평균보다 클 때만 카운트
((평균보다 높은 점수의 학생 수) / (총 학생 수)) * 100 식을 이용하여, 평균보다 높은 점수를 받은 학생의 비율(%) 도출
비율 요소를 리스트에 추가하여
리스트 요소 반복 출력
'''
C = int(input())                                # 테스트케이스 입력값 저장
percentages = []                                # 평균 초과 비율 저장할 리스트
for i in range(C):                              # 테스트케이스 반복
    scores = list(map(int, input().split()))    # 학생 수와 점수 입력값 저장
    tot_score = 0                               # 총 점수 초기화
    cnt = 0                                     # 상위권 학생 수 초기화

    for score in scores[1:]:                    # 학생 점수 반복문 (총 점수 구하기 위함)
        tot_score += score                      # 학생 점수 다 더하기
    
    for score in scores[1:]:                    # 학생 점수 반복문
        if score > tot_score / scores[0]:       # 학생 점수가 평균점수보다 크면
            cnt += 1                            # 상위권 학생 수에 1 추가
    
    percentages += [(cnt / scores[0]) * 100]    # 평균 초과 비율 리스트에 비율 추가

for percent in percentages:                     # 평균 초과 비율 리스트에서
    print(f'{percent:.3f}%')                    # 각 비율 요소를 소수점 3자리 수로 변형하여 출력