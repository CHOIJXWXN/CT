'''
줄세우기
n을 뽑으면, 현재 자기 자리보다 n 앞으로 이동
'''
N = int(input())                        # 학생 수 입력값 저장
num = list(map(int, input().split()))   # 학생이 뽑은 뽑기 리스트 저장
order = []                              # 줄 세우는 리스트 초기화
for i in range(N):                      # 모든 학생 반복
    order.insert(i - num[i], i + 1)     # 본래 자신의 인덱스 i보다 n 앞의 인덱스에 삽입
print(*order)                           # 출력