'''
숨바꼭질
'''
import queue

# def bfs(n):
#     p.put(n)
#     cnt = 0
#     while p.empty():
#         l = p.qsize()
#         while l:
#             x = p.get()
#             if x == K:
#                 print(cnt)
#                 exit()
#             for nx in (x - 1, x + 1, 2 * x):
#                 if 0 <= nx <= 10 ** 5:
#                     p.put(nx)
#             l -= 1
#         cnt += 1

def bfs(n):
    p.put(n)
    while p:
        x = p.get()
        if x == K:
            print(d[x])
            exit()
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= (10 ** 5) and not d[nx]:
                p.put(nx)
                d[nx] = d[x] + 1

N, K = map(int, input().split())
p = queue.Queue()
d = [0] * (10 ** 5 + 1)
bfs(N)