'''
피노키오
a g t c 중 하나씩 고르는 경우의 수이므로 (위치에 따라 distinct)
각각의 개수를 곱한 값이 곧 조합의 수
'''
L = int(input())                            # 염기열의 길이 입력값 저장
S = input()                                 # 염기열 입력값 저장
genes = ['A', 'G', 'T', 'C']                # 염기 종류 리스트 정의
cnts = [S.count(gene) for gene in genes]    # 각각 염기 종류마다 개수를 리스트에 저장
result = 1                                  # 곱 변수 초기화
for cnt in cnts:                            # 각각 염기의 개수를
    result *= cnt                           # 모두 곱함
print(result % 1000000007)                  # 곱한 값 반환 (문제의 조건에 따라 특정 큰 숫자의 나머지로 반환)