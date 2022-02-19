'''
나머지
10개의 숫자 중 42로 나눈 나머지 distinct 개수
'''
r = [0]*42                  # 인덱스가 0~41인 리스트 생성
for i in range(10):         # 열 번 반복
    num = int(input())      # 입력값 저장
    r[num % 42] = 1         # 해당 숫자를 42로 나눈 나머지를 인덱스로 하는 값을 1로 업데이트
print(sum(r))               # 리스트의 요소 모두 더하기