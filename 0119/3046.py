'''
R2
R1과 R2의 평균이 S이므로
R1 + R2 = 2 * S
R2 = 2 * S - R1
'''
R1, S = map(int, input().split())   # 입력값 저장
print(2 * S - R1)                   # 계산식 출력