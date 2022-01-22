'''
도비의 영어 공부
#가 나올 때까지 무한 반복 (#가 나오면 중단)
알파벳과 문장 입력값 저장
알파벳의 대문자와, 대문자로 변형된 문장의 요소 하나하나와 비교
일치한다면 카운트
각 카운트를 리스트에 저장하여
처음에 입력된 알파벳과 카운트 출력
'''
results = []                                # 입력 알파벳과 카운트 저장할 리스트
while True:                                 # 무한 반복
    sentence = input()                      # 입력값 저장
    cnt = 0                                 # 일치 알파벳 개수 초기화
    
    if sentence == '#':                     # 입력값이 #이면
        break                               # 반복 탈출
    
    for char in sentence[1:].upper():       # 대문자로 변형된 문자열 반복
        if sentence[0].upper() == char:     # 입력 알파벳 대문자와 문자열 요소가 같으면
            cnt += 1                        # 카운트 추가
    
    results += [[sentence[0], cnt]]         # 입력 알파벳과 카운트를 리스트에 추가

for result in results:                      # 리스트를 반복하여
    print(result[0], result[1])             # 입력 알파벳과 카운트를 출력