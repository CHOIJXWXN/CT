'''
안테나
중간값?
'''
N = int(input())
p = sorted(list(map(int, input().split())))
if N % 2:
    m = p[N // 2]
else:
    m1, m2 = p[N // 2 - 1], p[N // 2]
    c1, c2 = p.count(m1), p.count(m2)
    if c1 >= c2 :
        m = m1
    elif c1 < c2 :
        m = m2
print(m)