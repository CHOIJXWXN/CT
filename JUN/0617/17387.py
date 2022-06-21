"""
선분 교차 2
사실은 ccw로 풀어야 하는 문제랍니다
"""
import sys
read = sys.stdin.readline

x1, y1, x2, y2 = map(int, read().split())
x3, y3, x4, y4 = map(int, read().split())
X1, X2, X3, X4, Y1, Y2, Y3, Y4 = min(x1, x2), max(x1, x2), min(x3, x4), max(x3, x4), min(y1, y2), max(y1, y2), min(y3, y4), max(y3, y4)
# 평행일 때
if (x3 - x4) * (y1 - y2) == (x1 - x2) * (y3 - y4):
    # 두 직선 도메인이 안 맞으면
    if X2 < X3 or X1 > X4 or Y2 < Y3 or Y1 > Y4:
        print(0)
    else:
        # 평행이긴 한데 안 겹치면
        if (x1 - x3) * (y2 - y4) == (x2 - x4) * (y1 - y3):
            print(1)
        else:
            print(0)
    exit()
# 교차점 x, y
x = ((x3 - x4) * (x2 * y1 - x1 * y2) + (x1 - x2) * (x3 * y4 - x4 * y3)) / ((y1 - y2) * (x3 - x4) - (y3 - y4) * (x1 - x2))
if x1 == x2:
    y = y3 + (y3 - y4) * (x - x3) / (x3 - x4)
else:
    y = y1 + (y1 - y2) * (x - x1) / (x1 - x2)
# x, y가 선분 위에 존재하는지
print(int(X1 <= x <= X2 and X3 <= x <= X4 and Y1 <= y <= Y2 and Y3 <= y <= Y4))
