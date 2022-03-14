'''
2017 연세대학교 프로그래밍 경시대회
'''
N = int(input())
cnt = 0
T = 1
while T < N - 4:
    cnt += (N - 3 - T) // 2
    T += 2
print(cnt)