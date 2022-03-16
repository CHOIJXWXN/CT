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

        for nx in range(x + 1, x + 7):                      # 주사위는 1부터 6까지이므로 현재 좌표에 이를 더한 범위 반복
            if nx <= 100 and not d[nx] and not d[m[nx]]:    # 이동한 좌표가 100이하이고, 방문한 적이 없으며, 뱀/사다리로 이동할 좌표 또한 방문한 적이 없다면
                if m[nx]:                                   # 사다리 혹은 뱀이 있다면
                    nx = m[nx]                              # 이동 좌표 한 번 더 옮기기
                d[nx] = d[x] + 1                            # 이동 횟수 + 1 
                p.put(nx)

N, M = map(int, input().split())            # 사다리 수, 뱀 수 입력값 저장
m = [0] * 101                               # 사다리 혹은 뱀이 있는 좌표와 그 좌표에 도착하면 이동해야 하는 좌표 저장 / 사다리가 1에서 99로 놓여있다면 m[1] = 99
d = [0] * 101                               # 각 좌표마다 몇 번째 이동인지 저장 / 세 번 이동한 현재 좌표가 19라면 d[19] = 3
p = queue.Queue()
for _ in range(N):                          # 사다리 좌표 저장
    x, y = map(int, input().split())
    m[x] = y
for _ in range(M):                          # 뱀 좌표 저장
    u, v = map(int, input().split())
    m[u] = v

bfs(1)                                      # 1에서 시작