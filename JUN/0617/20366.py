"""
같이 눈사람 만들래?
투포인터
N개 중에 4개 선택?
s1 = 0, e1 = N - 1 해두고
s2 = 1, e2 = N - 2 로 돌리나?
"""
import sys
read = sys.stdin.readline

N = int(read())
D = list(map(int, read().split()))
D.sort()
s1, e1 = 0, N - 1
ans = 2 * 10**9
for s1 in range(N - 3):
    for e1 in range(s1 + 3, N):
        d1 = D[s1] + D[e1]
        s2, e2 = s1 + 1, e1 - 1
        while s2 < e2:
            d2 = D[s2] + D[e2]
            ans = min(ans, abs(d1 - d2))
            if d1 - d2 > 0:
                s2 += 1
            elif d1 - d2 < 0:
                e2 -= 1
            else:
                break
print(ans)