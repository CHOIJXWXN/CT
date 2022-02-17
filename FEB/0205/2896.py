'''
무알콜 칵테일
'''
juice = list(map(int, input().split()))     # 주스 양 입력값 저장
ratio = list(map(int, input().split()))     # 비율 입력값 저장
min_q = min(juice[i]/ratio[i] for i in range(len(juice)))   # 주스양/비율 값 중 가장 작은 값 저장
# min_q * 비율(얘는 float이므로)과 원래 주스 양의 차가 0.000001보다 작다면 0
# 그렇지 않으면 소수점 6자리까지만 저장
result = [0 if abs(ratio[i] * min_q - juice[i]) < 1e-6 else round(juice[i] - ratio[i] * min_q, 6) for i in range(len(ratio))]
print(*result)  # 출력