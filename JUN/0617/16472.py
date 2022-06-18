"""
고냥이
투포인터
"""
import sys
read = sys.stdin.readline


def idx(char):
    return ord(char) - ord('a')


N = int(read())
S = list(read().rstrip())
lenS = len(S)
lenSS = len(set(S))
if lenSS <= N:
    print(lenS)
    exit()
alph = [0] * 26
s, e = 0, 1
alph[idx(S[s])] += 1
alph[idx(S[e])] += 1
cnt, max_len = 2, 0
if S[s] == S[e]:
    cnt = 1
while s < e:
    if cnt <= N:
        if cnt == N:
            max_len = max(max_len, e - s + 1)
        e += 1
        if e == lenS:
            break
        if not alph[idx(S[e])]:
            cnt += 1
        alph[idx(S[e])] += 1
    elif cnt > N:
        alph[idx(S[s])] -= 1
        if not alph[idx(S[s])]:
            cnt -= 1
        s += 1
print(max_len)
