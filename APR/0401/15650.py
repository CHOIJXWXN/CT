'''
N과 M(2)
'''
def comb(cnt, start):
    if cnt == M:
        print(*l)
        return
    for i in range(start, N):
        l[cnt] = L[i]
        comb(cnt + 1, i + 1)

N, M = map(int, input().split())
L = [i for i in range(1, N + 1)]
l = [0] * M
comb(0, 0)