'''
팩토리얼
반복문 이용하여 1에서 입력값만큼 곱한 값 출력
'''
N = int(input())        # 입력값 저장
fact = 1                # 팩토리얼 초기화
for i in range(N):      # 입력값만큼 반복
    fact *= i + 1       # 곱하기
print(fact)             # 팩토리얼 출력