'''
하노이 탑 이동 순서
규칙 :   N개의 블록이 있으면
        N-1개의 블록 -> B
        N번째 블록 -> C
        B에 있던 N-1개의 블록 -> C
        이것의 반복
'''

N = int(input())                    # 입력값 저장

def hanoi(cnt, start, mid, end):    # 하노이 함수 (매개변수는 블록개수, 시작지점, 중간지점, 도착지점)
    if cnt == 1:                    # cnt = 1일 때 정의
        return [[start, end]]       # A에서 C로 이동 (자명)
    else:                           # 그 외 경우에는 위 주석의 규칙에 따름
        return hanoi(cnt - 1, start, end, mid) + [[start, end]] + hanoi(cnt - 1, mid, start, end)
                 # cnt - 1개의 블록이 A에서 B로    # cnt번째 블록을 A에서 C로   # cnt - 1개의 블록이 B에서 C로

print(len(hanoi(N, 1, 2, 3)))       # 해당 함수 반환 리스트의 총 길이 출력
for pair in hanoi(N, 1, 2, 3):      # 함수 요소 출력을 위해 반복문
    print(pair[0], pair[1])         # 함수 요소의 첫번째와 두번째 요소 출력