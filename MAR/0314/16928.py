'''
뱀과 사다리 게임
'''
import queue

def bfs(n):
    p.put(n)
    while p:
        x = p.get()
        if x == 100:
            print(d[x])
            exit()
        for nx in range(x + 1, x + 7):
            if nx <= 100 and not d[nx] and not d[m[nx]]:
                if m[nx]:
                    nx = m[nx]
                d[nx] = d[x] + 1
                p.put(nx)

N, M = map(int, input().split())
m = [0] * 101
d = [0] * 101
p = queue.Queue()
for _ in range(N):
    x, y = map(int, input().split())
    m[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    m[u] = v

bfs(1)