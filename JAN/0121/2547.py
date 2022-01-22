'''
사탕선생 고창영
테스트 케이스 반복문 안에 사탕 개수 반복문
각각 테스트 케이스마다 사탕 수가 학생 수에 나누어떨어지는지 판별
판별 플래그를 리스트에 저장해서
플래그 반복 출력
'''

T = int(input())                    # 테스트케이스 입력값 저장
ans = []                            # 판별 플래그를 저장할 리스트

for i in range(T):                  # 테스트케이스 하나씩 반복
    blank = input()                 # 빈 줄 넘기기
    N = int(input())                # 학생 수 입력값 저장
    candies = 0                     # 사탕 수 초기화

    for j in range(N):              # 학생 수만큼 반복 (총 사탕 수 얻기 위함)
        candies += int(input())     # 사탕 수 다 더하기

    if candies % N:                 # 총 사탕 수가 학생 수로 나누어 떨어지지 않으면
        ans.append('NO')            # 판별 플래그 리스트에 NO 추가
    else:                           # 총 사타 수가 학생 수로 나누어 떨어지면
        ans.append('YES')           # 판별 플래그 리스트에 YES 추가

for k in range(T):                  # 테스트케이스마다 저장된
    print(ans[k])                   # 판별 플래그 출력