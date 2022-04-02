'''
N과 M(3)
'''
def perm(cnt):
    if cnt == M:
        print(*l)
        return
    for i in range(N):
        l[cnt] = L[i]
        perm(cnt + 1)

N, M = map(int, input().split())
L = [i for i in range(1, N + 1)]
l = [0] * M
perm(0)