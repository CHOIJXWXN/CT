'''
시그마
'''
# 1부터 n까지 더하기 = (1 + n) * n / 2
A, B = map(int, input().split())    # 두 수 입력값 저장
C = A - B if A > B else B - A       # abs(A - B) 저장
print((A + B) * (C + 1) // 2)       # 가우스 출력