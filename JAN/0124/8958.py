'''
OX퀴즈
연속 O가 나올 때는 누적 + 1
즉, O가 두 번 연속으로 나오면 총 점수는 3, O가 네 번 연속으로 나오면 총 점수는 10
'''
T = int(input())                        # 테스트케이스 입력값 저장
scores = []                             # 각 테스트케이스마다 점수를 저장할 리스트

for i in range(T):                      # 테스트케이스 반복
    marks = input().split('X')          # 받는 문자열을 X로 나누기 (OXOOXXO -> ['O', 'OO', '', 'O']) 아마..
    score = 0                           # 점수 초기화
    
    for mark in marks:                  # 리스트 반복
        n = len(mark)                   # 요소의 길이 저장
        score += (n * (n + 1)) // 2     # 점수에 더하기
    
    scores.append(score)                # 리스트에 점수 추가

for score in scores:
    print(score)                        # 점수 출력