'''
통학의 신
근의 공식
'''
A, B = map(int, input().split())                                    # A, B 입력값 저장
C = A**2 - B                                                        # 자주 쓰이는 값 C로 저장
print(int(-A - C ** 0.5), int(-A + C ** 0.5)) if C else print(-A)   # 중근이면 -A 출력, 아니면 두 개 출력