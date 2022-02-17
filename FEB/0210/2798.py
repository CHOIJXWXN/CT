'''
블랙잭
3개 골라서 그 합이 M과 가장 가까운 수 출력 (M보다 작아야 함)
'''
N, M = map(int, input().split())                            # N, M 입력값 저장
cards = list(map(int, input().split()))                     # 카드 입력값 저장

min_diff = M                                                # M과의 차가 제일 커봤자 M이므로 최솟값 초기화
tot = cards[0] + cards[1] + cards[2]                        # 세 카드의 합 초기화

for i in range(N - 2):                                      # 0부터 N - 3까지 반복
    for j in range(i + 1, N - 1):                           # i + 1부터 N - 2까지 반복
        for k in range(j + 1, N):                           # j + 1부터 N - 1까지 반복

            diff = M - (cards[i] + cards[j] + cards[k])     # 그렇게 고른 세 카드의 합과 M의 차 계산

            if min_diff > diff >= 0:                        # 차가 0보다 크거나 같고 최소 차보다 작으면
                min_diff = diff                             # 최소 차 업데이트
                tot = cards[i] + cards[j] + cards[k]        # 이 때 세 카드의 합도 업데이트

print(tot)                                                  # 세 카드의 합 출력