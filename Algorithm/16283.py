'''
Farm
양 s, 염소 g
s + g = n
s * a + g * b = w
s * a + g * a = n * a
g * (b - a) = w - n * a
g = (w - n * a) / (b - a)
'''
a, b, n, w = map(int, input().split())
if a == b:
    if n == 2 and 2 * a == w:
        print(1, 1)
    else:
        print(-1)
else:
    g = (w - n * a) // (b - a)
    if (w - n * a) % (b - a) or g == n or g == 0:
        print(-1)
    else:
        print(n - g, g)