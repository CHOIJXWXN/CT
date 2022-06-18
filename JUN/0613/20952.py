"""
게임 개발자 승희
"""
# 시간 초과

# import sys
# read = sys.stdin.readline
# N, M = map(int, read().split())
# A = list(map(int, read().split()))
# B = list(map(int, read().split()))
# len_AR = N
# rm = list()
# for m in range(M):
#     r, temp_rm = 0, list()
#     for n in range(N):
#         if not (A[n] + B[m]) % 7:
#             r += 1
#             temp_rm.append(n)
#     if r == len_AR:
#         temp_rm.clear()
#         continue
#     for n in range(N):
#         A[n] += B[m]
#     len_AR -= r
#     rm.extend(temp_rm)
# print(len_AR)
# for n in range(N):
#     if n not in rm:
#         print(A[n] % (10**9 + 7), end=' ')

import sys
read = sys.stdin.readline
N, M = map(int, read().split())
A = list(map(int, read().split()))
B = list(map(int, read().split()))
r = [0] * 7                             # 나머지 배열
for a in A:
    r[a % 7] = 1
add = 0                                 # 최종적으로 더해줄 값
for b in B:
    add += b
    temp = [0] * 7                      # 임시 나머지 배열
    for i in range(7):
        if r[i] and (i + add) % 7:      # 더했을 때 7로 나누어떨어지지 않으면
            temp[i] = 1                 # 임시 나머지 배열에 저장
    if sum(temp):                       # 단 하나라도 7과 나누어 떨어지지 않는 수가 있다면
        r = temp                        # 나머지 배열 업데이트
    else:                               # 모두 나누어떨어진다면 (모두 원래 배열에서 제거된다면)
        add -= b                        # 해당 값은 더해주지 않음
ans = list()
for a in A:
    if r[a % 7]:                                # 나머지 배열에 존재하는 요소들만
        ans.append((a + add) % (10**9 + 7))     # 출력 배열에 저장
print(len(ans))
print(*ans)