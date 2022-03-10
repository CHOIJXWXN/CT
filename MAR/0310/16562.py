'''
친구비

1. 친구 그룹 (연결요소) 찾기
2. 그룹마다 최소 친구비 구하기
3. 다 더하기
4. K보다 작으면 다 내고 K보다 많으면 찐따되기
'''
import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    min_fee = fee[n - 1]
    visited[n] = True
    for friend in friends[n]:
        if not visited[friend]:
            min_fee = min(min_fee, dfs(friend))         # 2
    return min_fee

N, M, K = map(int, input().split())
fee = list(map(int, input().split()))
visited = [False for _ in range(N + 1)]
friends = [list() for _ in range(N + 1)]
tot_fee = 0
for _ in range(M):
    v, w = map(int, input().split())
    friends[v].append(w)
    friends[w].append(v)
for i in range(1, N + 1):                               # 1
    if not visited[i]:
        tot_fee += dfs(i)                               # 3
print(tot_fee) if K >= tot_fee else print('Oh no')      # 4