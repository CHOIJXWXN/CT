"""
날카로운 눈
"""
import sys

read = sys.stdin.readline


# A 이상 m 이하의 수 중 카운트되는 숫자의 개수
def cnt(m):
    total = 0
    for i in range(N):
        if m >= arr[i][0]:
            total += ((min(arr[i][1], m) - arr[i][0]) // arr[i][2]) + 1
    return total


N = int(read())
arr = [list(map(int, read().split())) for _ in range(N)]
b = 0
t = 2147483648
# 이분 탐색으로 자신 이하의 수의 개수가 홀수개인 최소 수를 찾는다
while b < t:
    mid = (b + t) // 2
    if not cnt(mid) % 2:
        b = mid + 1
    else:
        t = mid
if b == 2147483648:
    print('NOTHING')
else:
    print(b, cnt(b) - cnt(b - 1))