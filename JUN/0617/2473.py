"""
세 용액
"""
import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))
arr.sort()
min_ph = abs(arr[0] + arr[1] + arr[2])
min_pair = (arr[0], arr[1], arr[2])
for i in range(N - 2):
    s, e, p = i + 1, N - 1, arr[i]
    while s < e:
        ph = arr[s] + arr[e] + p
        if min_ph > abs(ph):
            min_ph = abs(ph)
            min_pair = (arr[i], arr[s], arr[e])
        if ph < 0:
            s += 1
        elif ph > 0:
            e -= 1
        else:
            break
print(*min_pair)
