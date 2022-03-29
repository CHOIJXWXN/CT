'''
음하철도 구구팔
'''
import math

station = list(map(int, input().split()))
x, y, dx, dy = map(int, input().split())
r = math.gcd(dx, dy)
dx //= r
dy //= r
min_d, d = 400, math.sqrt((station[0] - x) ** 2 + (station[1] - y) ** 2)
while True:
    min_d = min(d, min_d)
    x += dx
    y += dy
    d = math.sqrt((station[0] - x) ** 2 + (station[1] - y) ** 2)
    if min_d < d:
        print(x - dx, y - dy)
        break