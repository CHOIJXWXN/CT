'''
숨바꼭질
'''
import queue

# def bfs(n):
#     p.put(n)
#     cnt = 0
#     '''
#     2                                   l = 0
#     1,          3,          4           l = 1
#     0, 2       2, 4, 6     3, 5, 8      l = 2
#     '''
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
    p.put(n)                # 현재 수빈이 위치를 큐에 추가
    while p:                # 큐가 빌 때까지
        x = p.get()         # 큐의 첫번째 요소 빼기
        if x == K:          # 해당 좌표가 동생이 있는 좌표라면
            print(d[x])     # 지금 좌표가 몇 번의 이동으로 도착한 건지 출력
            exit()          # 프로그램 종료
        for nx in (x - 1, x + 1, 2 * x):                # 현재 수빈이가 갈 수 있는 좌표들 반복
            if 0 <= nx <= (10 ** 5) and not d[nx]:      # 범위 안에서 벗어나지 않고 한 번 가본 좌표가 아니라면
                p.put(nx)                               # 이동 가능한 좌표들 모두 큐에 추가
                d[nx] = d[x] + 1                        # 한 번 이동했으므로 이동한 횟수 + 1

N, K = map(int, input().split())
p = queue.Queue()
d = [0] * (10 ** 5 + 1)             # 수빈이 위치와 순서, 수빈이가 두 번째로 간 좌표가 10이라면 d[10] = 2
bfs(N)