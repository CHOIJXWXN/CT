'''
문자열 반복
'''
T = int(input())                        # 테스트케이스 입력값 저장
for i in range(T):                      # 테스트케이스 반복
    R, S = map(str, input().split())    # 반복횟수와 문자열 입력값 저장
    result = ''                         # 출력할 문자열
    for s in S:                         # 입력 받은 문자열의 요소 반복
        result += s * int(R)            # 출력할 문자열에 해당 문자열 요소를 R번 반복
    print(result)                       # 출력