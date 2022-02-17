'''
단어순서 뒤집기
스페이스 기준으로 나눠서 뒤에서부터 출력
'''
# N = int(input())
# for i in range(N):
#     sentence = list(map(str, input().split()))
#     result = ''
#     for word in sentence:
#         result = word + ' ' + result
#     print('Case #' + str(i + 1) + ': ' + result)

N = int(input())                                    # 테스트케이스 입력값 저장

for i in range(N):                                  # 모든 테스트케이스 반복
    sentence = list(map(str, input().split()))      # 한 문장을 스페이스 기준으로 단어를 나누어 리스트에 저장

    print('Case #' + str(i + 1) + ': ', end = '')   # 테스트케이스 표시 출력

    for i in range(len(sentence)):                  # 문장 속 단어 반복
        print(sentence.pop(), end = ' ')            # 뒤에서부터 하나씩 빼서 출력