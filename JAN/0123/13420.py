'''
사칙연산
space를 기준으로 문자열을 나누어 각각 저장
연산자를 비교해 각각 사칙연산 검증 후 출력
'''
N = int(input())                                        # 테스트케이스 입력값 저장
results = []                                            # 판별 플래그 저장할 리스트
for i in range(N):                                      # 테스트케이스 반복
    num1, calc, num2, eq, ans = input().split(' ')      # 숫자1, 연산자, 숫자2, 등호, 숫자3 입력값 저장
    if calc == '+':                                     # 덧셈일 때
        flag = (int(num1) + int(num2) == int(ans))      # 더해준 값이 맞는지 판별 후 참거짓 저장
    elif calc == '-':
        flag = (int(num1) - int(num2) == int(ans))
    elif calc == '*':
        flag = (int(num1) * int(num2) == int(ans))
    elif calc == '/':
        flag = (int(num1) / int(num2) == int(ans))
    results.append(flag)                                # 참거짓을 리스트에 저장

for result in results:                                  # 결과값 반복
    if result:                                          # 참일 때
        print('correct')                                # correct 출력
    else:                                               # 거짓일 때
        print('wrong answer')                           # wrong answer 출력