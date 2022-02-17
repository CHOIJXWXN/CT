'''
탄산 음료
'''
e, f, c = map(int, input().split())     # 빈 병, 주운 병, 필요한 병 입력값 저장

have = e + f                            # 가지고 있는 병 개수
buy = 0                                 # 살 수 있는 병 개수
tot = 0                                 # 실제로 산 병 개수

while True:                 # 무한 반복
    
    if not have // c:       # 현재 가지고 있는 병으로 새로 병을 살 수 없을 때
        break               # 반복문 탈출

    buy = have // c         # 현재 살 수 있는 병 계산
    tot += buy              # 실제로 산 병에 추가
    have %= c               # 현재 가지고 있는 병 업데이트 (새로 사느라 써버린 병 빼기)
    have += buy             # 현재 가지고 있는 병 업데이트 (새로 산 병 더하기)

print(tot)                  # 실제로 산 병 개수 출력