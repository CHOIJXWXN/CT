'''
창영이의 일기장
앞에서부터 모음이 나오면 해당 모음 뒤 두 글자 삭제
반복
'''
diary = input()                                 # 일기 입력값 저장
idx = 0                                         # 인덱스 초기화
while idx < len(diary):                         # 인덱스가 길이보다 작을 때 반복
    if diary[idx] in 'aeiou':                   # 다이어리의 인덱스번째 글자가 모음이면
        diary = diary[:idx+1] + diary[idx+3:]   # 뒤에 두 글자 삭제
    idx += 1                                    # 인덱스 + 1
print(diary)                                    # 일기 출력