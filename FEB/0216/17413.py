'''
단어 뒤집기 2
<...> 꺽쇠 안에 들어있는 문자열은 그대로 출력 / 그 외에는 공백을 기준으로 단어마다 거꾸로 출력
'''
S = input()     # 입력값 저장
word = ''       # 공백을 기준으로 한 단어를 뒤집기 위한 문자열
result = ''     # 최종 출력할 문자열
flag = False    # 똑바로 출력하는가, 반대로 출력하는가 판단하는 플래그 (시작은 반대로)

for char in S:                          # 모든 문자 반복

    if flag:                            # 똑바로 출력해야한다면
        result += char                  # 최종 출력 문자열에 현재 문자 추가
        
        if char == '>':                 # 이 문자가 닫는 꺽쇠라면
            result = word + result      # 지금까지 꺽쇠 밖의 단어를 최종 출력 문자열에 추가
            word = ''                   # 단어 초기화
            flag = False                # 이제 다시 거꾸로 출력해야하므로 플래그 전환
    
    else:                               # 반대로 출력해야한다면
        
        if char == '<':                 # 이 문자가 여는 꺽쇠라면
            result += word + char       # 최종 출력 문자열에 지금까지 단어와 여는 꺽쇠 추가
            flag = True                 # 이제 다시 똑바로 출력해야하므로 플래그 전환
            word = ''                   # 단어 초기화
        
        elif char == ' ':               # 이 문자가 space라면
            result += word + ' '        # 최종 출력 문자열에 앞의 뒤집힌 단어와 space 추가
            word = ''                   # 단어 초기화

        else:                           # 일반적인 숫자 혹은 알파벳이라면
            word = char + word          # 단어 앞에 문자 추가

print(result + word)                    # 최종 출력물과 마지막 단어까지 추가해서 출력