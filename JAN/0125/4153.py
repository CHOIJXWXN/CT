'''
직각삼각형
세 변의 길이가 주어졌을 때 직각인지 구하는 문제
변 길이 리스트를 정렬한 뒤 피타고라스 이용
'''
while True:                                             # 무한 반복
    lens = list(map(int, input().split()))              # 길이 리스트 입력값 저장
    if lens == [0] * 3:                                 # 0 0 0을 입력했을 때
        break                                           # 반복문 탈출
    lens.sort()                                         # 길이 오름차순 정렬
    if lens[0] ** 2 + lens[1] ** 2 == lens[2] ** 2:     # 피타고라스 만족하면
        print('right')                                  # right 출력
    else:                                               # 만족하지 않으면
        print('wrong')                                  # wrong 출력