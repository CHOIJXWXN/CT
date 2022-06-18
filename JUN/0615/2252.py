"""
줄 세우기
가장 작은 학생부터 거슬러 올라가기
"""

# 아래 예시 충족 X
# 4 3
# 3 2
# 2 1
#
# 8 7
# 7 6
# 6 5
# 5 3
#
# 4 ------------ 3 - 2 - 1
# 8 - 7 - 6 - 5 -|

# import sys
# from collections import deque
#
# read = sys.stdin.readline
#
# N, M = map(int, read().split())
# tall = [list() for _ in range(N + 1)]
# short = [0] * (N + 1)
# v = [False] * (N + 1)
# for _ in range(M):
#     A, B = map(int, read().split()) # A가 B보다 앞에 서야 한다.
#     tall[A].append(B)
#     short[B] += 1
# q = deque()
# for n in range(1, N + 1):
#     if not short[n]:
#         q.append(n)
#         v[n] = True
# while q:
#     x = q.popleft()
#     print(x, end=' ')
#     for t in tall[x]:
#         if not v[t]:
#             q.append(t)
#             v[t] = True

# short 활용
# pypy가 더 느린 매직
import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())         # 학생수 / 비교수 입력
tall = [list() for _ in range(N + 1)]   # idx보다 큰 학생의 idx 저장할 리스트  ex) tall[1] = [2, 3] : 1보다 2, 3이 더 크다
short = [0] * (N + 1)                   # idx보다 작은 학생의 수를 저장할 리스트 ex) short[4] = 2 : 4보다 작은 학생이 두 명 있다
for _ in range(M):
    A, B = map(int, read().split())     # A가 B보다 앞에 서야 한다
    tall[A].append(B)
    short[B] += 1
# bfs
q = deque()
for n in range(1, N + 1):
    if not short[n]:                    # 자신보다 작은 학생이 없는 학생들을 q에 추가
        q.append(n)
while q:
    x = q.popleft()
    print(x, end=' ')                   # 현재 집단에서 가장 작은 학생들 출력
    for t in tall[x]:                   # 해당 학생보다 큰 학생들 중에서
        short[t] -= 1                   # 해당 학생이 빠지고서
        if not short[t]:                # 자신보다 작은 학생이 더이상 없는 학생들만
            q.append(t)                 # q에 추가
