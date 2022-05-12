'''
LCS 2
'''
# 둘 다 저장
# python : 2508ms
# pypy   : 1216ms

# N = input()
# M = input()
# n, m = len(N), len(M)
# d = [[[0, ''] for _ in range(m + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if N[i - 1] == M[j - 1]:
#             d[i][j][0] = d[i - 1][j - 1][0] + 1
#             d[i][j][1] = d[i - 1][j - 1][1] + N[i - 1]
#         else:
#             if d[i - 1][j][0] > d[i][j - 1][0]:
#                 d[i][j][0] = d[i - 1][j][0]
#                 d[i][j][1] = d[i - 1][j][1]
#             else:
#                 d[i][j][0] = d[i][j - 1][0]
#                 d[i][j][1] = d[i][j - 1][1]
# print(d)
# print(*d[-1][-1], sep='\n') if d[-1][-1][0] else print(0)

# 문자열만 저장
# python : 2616ms
# pypy   : 558ms    (????)
N = input()
M = input()
n, m = len(N), len(M)
d = [['' for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if N[i - 1] == M[j - 1]:
            d[i][j] = d[i - 1][j - 1] + N[i - 1]
        else:
            if len(d[i - 1][j]) > len(d[i][j - 1]):
                d[i][j] = d[i - 1][j]
            else:
                d[i][j] = d[i][j - 1]
print(d)
l = len(d[-1][-1])
print(l, d[-1][-1], sep='\n') if l else print(0)
