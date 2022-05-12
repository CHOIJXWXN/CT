'''
가장 긴 짝수 연속한 부분 수열 (large)
'''
import sys

read = sys.stdin.readline
N, K = map(int, read().split())
A = list(map(int, read().split()))
for i in range(N):
    A[i] %= 2                           # 짝수는 0, 홀수는 1로 변환
print(A)
s, e = 0, 0                             # 투 포인터
sum, l = A[s], 1                        # sum은 합이므로 홀수의 개수, l은 길이
while s <= e:
    if sum > K:
        if s == e:                      # 현재 수열의 길이가 1임에도 홀수의 개수를 초과한다면
            e += 1                      # s와 e를 모두 옮겨줌
            sum += A[e]
        sum -= A[s]                     # 단순히 홀수의 개수를 초과한다면 s만 옮겨줌
        s += 1
    else:
        l = max(l, e - s + 1)           # 길이값 업데이트
        if e == N - 1:                  # e가 마지막에 도달했다면 종료
            break
        e += 1                          # 그렇지 않으면 e를 옮겨줌
        sum += A[e]
print(l - sum)                          # 짝수 길이는 전체 길이에서 홀수 개수를 빼준 것이므로 l - sum 출력