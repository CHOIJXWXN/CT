"""
용액
"""
import sys
read = sys.stdin.readline
N = int(read())
arr = list(map(int, read().split()))
s, e = 0, N - 1
min_ph = abs(arr[s] + arr[e])
min_pair = (arr[s], arr[e])
while s < e:
    ph = arr[s] + arr[e]
    if min_ph > abs(ph):
        min_ph = abs(ph)
        min_pair = (arr[s], arr[e])
    if ph < 0:
        s += 1
    elif ph > 0:
        e -= 1
    else:
        break
print(*min_pair)