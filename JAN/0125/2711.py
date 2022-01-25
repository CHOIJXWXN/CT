'''
오타맨 고창영
오타 낸 자리수를 인덱스로 활용해 slice
'''
T = int(input())                                    # 테스트케이스 입력값 저장
for i in range(T):                                  # 테스트케이스 반복
    idx, word = map(str, input().split())           # 오타 자리수와 단어 입력값 저장
    print(word[:int(idx) - 1] + word[int(idx):])    # 단어를 적절히 슬라이스하여 출력