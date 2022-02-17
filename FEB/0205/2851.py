'''
슈퍼 마리오
100이 될 때까지 버섯을 먹고, 100이 넘더라도 이전 포인트보다 100에 가깝거나 같다면 먹음
'''
tot = 0                                             # 총점 초기화
mushs = []                                          # 버섯 포인트 담을 리스트
for i in range(10):                                 # 10번 반복
    mushs.append(int(input()))                      # 입력값 리스트에 저장
for mush in mushs:                                  # 각 포인트 반복
    if abs(tot - 100) >= abs(tot + mush - 100):     # 현재 포인트와 100의 차가 나중 포인트와 100의 차보다 크거나 같다면
        tot += mush                                 # 버섯 먹음
    else:                                           # 아니면
        break                                       # 반복문 탈출
print(tot)                                          # 총점 출력