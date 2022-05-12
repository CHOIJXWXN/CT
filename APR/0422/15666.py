'''
N과 M(12)
'''
import sys

# 중복 조합 함수
def comb(cnt, start):
    if cnt == M:
        print(*l)
        return
    for i in range(start, lenA):
        l[cnt] = A[i]
        comb(cnt + 1, i)
        
read = sys.stdin.readline
N, M = map(int, read().split())
A = list(set(map(int, read().split())))     # set으로 받아 중복을 없애준 후 list로 형변환
lenA = len(A)                               # 중복 없는 숫자의 개수
A.sort()                                    # 오름차순 정렬
l = [0] * M                                 # 출력할 리스트
comb(0, 0)