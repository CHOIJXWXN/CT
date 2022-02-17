'''
수들의 합2
투포인터
연속된 n개의 수를 더했을 때 M이 되는 조합의 개수
인덱스 start = 0부터 end = 1부터 시작
start부터 end까지 더한 값이 { M보다 크면, start 미루기
                        M보다 작으면, end 미루기 }
                        M과 같으면 start와 end 동시에 미뤄서 새로 시작
'''
N, M = map(int, input().split())            # 수열 길이와 총합 입력값 저장
nums = list(map(int, input().split()))      # 수열 입력값 저장

# cnt = 0
# for i in range(N):
#     sum = 0
#     for j in range(i, N):
#         sum += nums[j]
#         if sum == M:
#             cnt += 1
#             break
# print(cnt)

cnt, start, end = 0, 0, 1                   # 조합 개수, 시작 인덱스, 끝 인덱스

while end <= N and start <= end:            # 끝 인덱스는 N 이하, 시작 인덱스는 끝 인덱스 이하일 때만 반복

    sumNums = sum(nums[start:end])          # 시작~끝 총합 계산

    if sumNums < M:                         # 총합이 M보다 작으면
        end += 1                            # 끝 인덱스 미루기
    
    elif sumNums > M:                       # 총합이 M보다 크면
        start += 1                          # 시작 인덱스 미루기
    
    else:                                   # M과 같으면
        cnt += 1                            # 개수 + 1
        start += 1                          # 시작 인덱스 미루기
        end += 1                            # 끝 인덱스 미루기

print(cnt)                                  # 개수 출력