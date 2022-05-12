'''
1로 만들기 2
'''
N = int(input())
if N == 1:
    print(0, 1, sep='\n')
    exit()
D = [[0] for _ in range(N + 1)]
for i in range(2, N + 1):
    d = 10**6
    idx = 0
    if i >= 1 and D[i - 1][0] + 1 < d:
        idx = i - 1
        d = D[idx][0] + 1
    if not i % 2 and D[i // 2][0] + 1 < d:
        idx = i // 2
        d = D[idx][0] + 1
    if not i % 3 and D[i // 3][0] + 1 < d:
        idx = i // 3
        d = D[idx][0] + 1
    D[i][0] = d
    D[i].append(idx)

ans = [N]
next = D[N][1]
cnt = D[N][0]

print(D)

for _ in range(cnt - 1):
    ans.append(next)
    next = D[next][1]

print(cnt)
print(*ans, 1)