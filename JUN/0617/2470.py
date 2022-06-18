"""
두 용액
2467 참고
"""
import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))
arr.sort()                                  # 입력값 오름차순 정렬
s, e = 0, N - 1                             # 투 포인터 시작~
min_ph = abs(arr[s] + arr[e])               # 최소 ph (절대값)
min_pair = (arr[s], arr[e])                 # 최소 ph일 때 두 용액 ph
while s < e:
    ph = arr[s] + arr[e]                    # 섞었을 때 ph
    if min_ph > abs(ph):                    # 가 최소 ph보다 작으면
        min_ph = abs(ph)                    # 최소 ph 업데이트
        min_pair = (arr[s], arr[e])         # 최소 ph일 때 두 용액 ph 업데이트
    if ph < 0:                              # ph가 0보다 작으면 s 올려주기
        s += 1
    elif ph > 0:                            # ph가 0보다 크면 e 내려주기
        e -= 1
    else:                                   # 0이면 더 할 필요 없으니까 탈출
        break
print(*min_pair)
