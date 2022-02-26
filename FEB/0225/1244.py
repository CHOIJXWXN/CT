'''
스위치 켜고 끄기
남학생 (1) : n의 배수 스위치
여학생 (2) : n을 기준으로 양 옆의 스위치 상태가 같으면 바꿔주기 반복 (n스위치 포함)
'''
N = int(input())
switch = list(map(int, input().split()))
n = int(input())
for i in range(n):
    gender, idx = map(int, input().split())
    # 남학생이면
    if gender == 1:
        i = 1
        while idx * i <= N:
            # abs(0 - 1) = 1, abs(1 - 1) = 0 즉, 0이면 1로 되고 1이면 0으로 바꿔주는 식
            switch[idx * i - 1] = abs(switch[idx * i - 1] - 1)
            i += 1
    else:
        i = 0
        while True:
            if idx - 1 - i < 0 or idx - 1 + i >= N:
                break
            if switch[idx - 1 - i] == switch[idx - 1 + i]:
                switch[idx - 1 - i], switch[idx - 1 + i] = abs(switch[idx - 1 - i] - 1), abs(switch[idx - 1 - i] - 1)
                i += 1
            else:
                break
for i in range(N):
    # 출력 형식 조건 꼭 확인할 것
    if i % 20 == 19:
        print(switch[i], end = '\n')
    else:
        print(switch[i], end = ' ')