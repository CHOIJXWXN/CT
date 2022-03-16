'''
교수가 된 현우
'''
import sys
T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    i = 5
    while True:
        if i > n:
            break
        cnt += n // i
        i *= 5
    print(cnt)