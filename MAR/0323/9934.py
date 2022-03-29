'''
완전 이진 트리
중위순회 리스트 입력 > 트리 출력

idx = 2 ** K

[1 2 3 4 5 6 7] 8 [9 10 11 12 13 14 15]

             8
     4               12
 2       6      10        14
1 3     5 7    9 11      13 15
'''
import sys

def mid(s, e, d):
    if d == K:
        return
    m = (s + e) // 2
    idx_list[d].append(v[m])
    mid(s, m, d + 1)
    mid(m, e, d + 1)

K = int(input())
v = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
idx_list = [list() for _ in range(K)]
mid(1, 2 ** K, 0)
for i in idx_list:
    print(*i)