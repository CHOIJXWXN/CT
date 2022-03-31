'''
퇴사
'''
N = int(input())
C = list()
for _ in range(N):
    C.append(list(map(int, input().split())))
C.append([0, 0])
D = [0] * (N + 5)
maxD = 0
for i in range(N + 1):
    D[i] = max(D[i], maxD)
    D[i + C[i][0]] = max(D[i + C[i][0]], D[i] + C[i][1])
    maxD = max(D[i], maxD)
print(maxD)

'''
백트래킹
'''
def recur(cur):
    total = 0
    if cur > N:
        return -100000
    if cur == N:
        return 0
    total = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    return total

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(recur(0))

'''
백트래킹 > DP
'''
dp = [-1 for _ in range(150010)]
def recur(cur):
    if cur > n:
        return -10000000
    if cur == n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    return dp[cur] 

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

print(recur(0))