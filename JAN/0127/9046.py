'''
복호화
가장 많이 사용된 알파벳을 찾는 프로그램
문자열에 사용된 모든 알파벳을 세어서 해당 알파벳 출력
개수가 똑같은 알파벳이 여러 개가 있으면 ? 출력
'''
T = int(input())        # 테스트케이스 입력값 저장
for i in range(T):      # 모든 테스트케이스 반복
    code = input()      # 암호 입력값 저장
    cnt = {}            # 알파벳 개수 저장할 빈 딕셔너리 초기화
    max_char = ''       # 가장 많은 알파벳 초기화
    for char in set(code.replace(' ', '')):   # 공백을 지운 암호 문자열 리스트를 세트로 변환하여 모든 알파벳 반복 (중복 제거를 위함)
        cnt[char] = code.count(char)          # 각 알파벳을 키로 하고 그 개수를 값으로 하여 딕셔너리에 저장
    max_cnt = max(cnt.values())               # 가장 많은 개수 저장
    for char, char_cnt in cnt.items():        # 딕셔너리의 모든 요소 반복
        if char_cnt == max_cnt:               # 딕셔너리의 값 중 가장 큰 값과 해당 요소의 값이 같다면
            if max_char:                        # max_char이 있으면 (즉, 같은 개수의 알파벳이 또 있으면)     
                max_char = '?'                  # max_char에 ? 저장
                break                           # 반복문 탈출
            else:                               # max_char이 비어있으면
                max_char = char                 # max_char에 해당 알파벳 저장
    print(max_char)                           # max_char 출력
    