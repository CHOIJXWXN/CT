'''
X보다 작은 수
입력 받은 리스트의 요소를 반복문을 이용하여
입력 받은 X와 하나하나 비교 (조건문 사용)
X보다 작은 요소는 출력
'''
N, X = map(int, input().split())        # 입력값 저장
A = list(map(int, input().split()))     # 입력값 저장
for a in A:                             # 입력 받은 리스트의 각 요소 반복
    if a < X:                           # 요소와 입력값 X 대소 비교
        print(a, end = ' ')             # 요소가 X보다 작으면 출력