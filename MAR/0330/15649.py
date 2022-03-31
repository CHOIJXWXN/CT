'''
N과 M (1)
'''
def perm(cnt):
    if cnt == M:
        print(*l)
        return
    for i in range(N):
        if not V[i]:
            l[cnt] = L[i]
            V[i] = True
            perm(cnt + 1)
            V[i] = False

N, M = map(int, input().split())
L = [i for i in range(1, N + 1)]
V = [False] * N
l = [0] * M
perm(0)