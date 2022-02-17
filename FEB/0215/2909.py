'''
캔디 구매
round 함수가 맨 마지막에 틀렸다고 나와서 직접 구현
해당하는 자리수로 끊어서 뒤에 자리수가 5 미만이면 버림, 5 이상이면 초과
'''
C, K = map(int, input().split())    # 두 수 입력값 저장
# print(round(C, -K))
q = C // (10 ** K)                  # 10의 K 제곱(자리수)으로 나눈 몫 저장
r = C % (10 ** K)                   # 10의 K 제곱(자리수)으로 나눈 나머지 저장
print(q * (10 ** K)) if r // (10 ** (K - 1)) < 5 else print((q + 1) * (10 ** K))
# 나머지의 첫 숫자가 5보다 작으면 몫 * 자리수 출력, 그 외에는 (몫 + 1) * 자리수 출력