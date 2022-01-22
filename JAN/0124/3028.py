'''
창영마을
문자열을 받은 후
A이면 첫 번째와 두 번째 교환
B이면 두 번째와 세 번째 교환
C이면 세 번째와 첫 번째 교환
'''
ball = [1, 0, 0]                                # 시작 리스트
order = input()                                 # 야바위 순서 입력값 저장
for char in order:                              # 문자열 반복
    if char == 'A':                             # A이면
        ball[0], ball[1] = ball[1], ball[0]     # [0]과 [1] 교환 (지금까지 발견한 자바보다 유일하게 좋은 점)
    elif char == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    elif char == 'C':
        ball[2], ball[0] = ball[0], ball[2]

for i in range(3):                              # 값이 1인 인덱스를 찾기 위한 반복문
    if ball[i] == 1:                            # 값이 1이면
        print(i + 1)                            # 해당 인덱스 + 1 출력