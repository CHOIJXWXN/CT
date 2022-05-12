'''
부분수열의 합 2
'''
import sys

def subset(cnt, arr, v, tot):
    if cnt == len(v):
        total = 0
        for i in range(cnt):
            if v[i]:
                total += arr[i]
        tot.append(total)
        return
    v[cnt] = True
    subset(cnt + 1, arr, v, tot)
    v[cnt] = False
    subset(cnt + 1, arr, v, tot)

read = sys.stdin.readline
N, S = map(int, read().split())
C = list(map(int, read().split()))
A, B, va, vb, totA, totB = C[:N // 2], C[N // 2:], [False] * (N // 2), [False] * (N - N // 2), list(), list()
subset(0, A, va, totA)
subset(0, B, vb, totB)
totA.sort()
totB.sort()
lenA, lenB = len(totA), len(totB)
idxA, idxB, cnt = 0, lenB - 1, 0
while idxA < lenA and idxB >= 0:
    sum = totA[idxA] + totB[idxB]
    if sum == S:
        cntA, cntB = 1, 1
        while idxA < lenA - 1 and totA[idxA] == totA[idxA + 1]:
            idxA += 1
            cntA += 1
        while idxB > 0 and totB[idxB] == totB[idxB - 1]:
            idxB -= 1
            cntB += 1
        cnt += cntA * cntB
        idxA += 1
        idxB -= 1
    elif sum < S:
        idxA += 1
    else:
        idxB -= 1
print(cnt) if S else print(cnt - 1)