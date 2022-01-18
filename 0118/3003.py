'''
킹, 퀸, 룩, 비숍, 나이트, 폰
각각 일정한 피스를 유지해야하므로
원하는 양에서 현재 가진 양을 뺀 양만큼 추가
'''
now = input().split()                           # 입력값
after = [1, 1, 2, 2, 2, 8]                      # 수량 조정 후 되어야 하는 양
for i in range(6):                              # 총 6개의 말 종류
    print(after[i] - int(now[i]), end = ' ')    # after - now 출력