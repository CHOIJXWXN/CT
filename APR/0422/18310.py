'''
안테나
'''
N = int(input())
p = list(map(int, input().split()))
p.sort()                                        # 오름차순 정렬
if N % 2:                                       # 홀수 개라면 중간값이 m
    m = p[N // 2]
else:                                           # 짝수 개라면
    m1, m2 = p[N // 2 - 1], p[N // 2]           # 두 개의 중간값
    c1, c2 = p.count(m1), p.count(m2)           # 중간값마다 개수
    m = m1 if c1 >= c2 else m2                  # 개수가 더 많은 것이 m
print(m)