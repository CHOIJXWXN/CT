"""
큐빙
"""
import sys
read = sys.stdin.readline


def turn(side):
    # + 기준
    if side == 'U':
        side, w, x, y, z = u, l, f, r, b
    elif side == 'D':
        side, w, x, y, z = d, b, r, f, l
    elif side == 'L':
        side, w, x, y, z = l, f, u, b, d
    elif side == 'R':
        side, w, x, y, z = r, d, b, u, f
    elif side == 'F':
        side, w, x, y, z = f, u, l, d, r
    elif side == 'B':
        side, w, x, y, z = b, r, d, l, u
    side[0][0], side[0][1], side[0][2], side[1][0], side[1][1], side[1][2], side[2][0], side[2][1], side[2][2] = \
        side[2][0], side[1][0], side[0][0], side[2][1], side[1][1], side[0][1], side[2][2], side[1][2], side[0][2]
    w[2][2], w[2][1], w[2][0], x[2][0], x[1][0], x[0][0], y[0][2], y[1][2], y[2][2], z[0][0], z[0][1], z[0][2] = \
        x[2][0], x[1][0], x[0][0], y[0][2], y[1][2], y[2][2], z[0][0], z[0][1], z[0][2], w[2][2], w[2][1], w[2][0]


T = int(read())
for _ in range(T):
    N = int(read())
    M = list(read().split())
    u, d, f, b, l, r = [['w'] * 3 for _ in range(3)],\
                       [['y'] * 3 for _ in range(3)],\
                       [['r'] * 3 for _ in range(3)],\
                       [['o'] * 3 for _ in range(3)],\
                       [['g'] * 3 for _ in range(3)],\
                       [['b'] * 3 for _ in range(3)]
    for m in M:
        turn(m[0])
        if m[1] == '-':
            turn(m[0])
            turn(m[0])
    for i in u:
        print(*i, sep='')
