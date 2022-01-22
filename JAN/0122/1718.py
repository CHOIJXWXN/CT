'''
암호
암호 전 입력값과 암호키 입력값 받고
아스키 코드 이용하여 정수형으로 변환 (a~z : 97~122)
암호키의 경우에는 정수형으로 변환한 후 96을 빼줘야 몇 번째 알파벳인지 알 수 있음
정수형 변환 시 97 미만으로 내려갈 경우에는 다시 z부터 시작해야하므로 26을 더해줌
space는 인코딩하지 않고 그대로 출력
인코딩된 암호화값 출력
'''
decode = input()                                                # 암호화 전 입력값 저장
key = input()                                                   # 암호화 키 입력값 저장
encode = ''                                                     # 암호화 후 문자열

for i in range(len(decode)):                                    # 암호화 전 입력값 길이만큼 반복
    asc_num = ord(decode[i]) - ord(key[i % (len(key))]) + 96    # 각 요소를 정수형으로 변환

    if decode[i] == ' ':                                        # space는 space 그대로
        alphabet = ' '
    elif asc_num < 97:                                          # 97 미만일 때
        alphabet = chr(asc_num + 26)                            # 26 더해줌
    else:                                                       # 97 이상일 때
        alphabet = chr(asc_num)                                 # 그대로

    encode += alphabet                                          # 암호화된 알파벳을 encode 문자열에 추가

print(encode)                                                   # 암호화된 문자열 출력