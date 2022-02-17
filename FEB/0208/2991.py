'''
사나운 개
0 < P % (A + B) <= A 이면 짖음
'''
A, B, C, D = map(int, input().split())  # 강아지 짖는 시간 / 조용한 시간 입력값 저장
men = list(map(int, input().split()))   # 세 사람이 오는 시간 입력값 저장

attack = [0]*3                          # 공격횟수 초기화

for i in range(3):                      # 세 사람 반복

    if 0 < men[i] % (A + B) <= A:       # 첫번째 강아지가 짖을 때 오면
        attack[i] += 1                  # 공격횟수 + 1

    if 0 < men[i] % (C + D) <= C:       # 두번째 강아지가 짖을 때 오면
        attack[i] += 1                  # 공격횟수 + 1

for i in range(3):                      # 공격횟수 반복 출력
    print(attack[i])
