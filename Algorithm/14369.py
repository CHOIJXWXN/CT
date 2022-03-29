'''
전화번호 수수께끼 (Small)
'''
import sys

N = int(input())
for i in range(1, N + 1):
    S = list(sys.stdin.readline())
    num = [0] * 10
          #   Z              W               U               X                G
    nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    while 'Z' in S:
        for n in nums[0]:
            S.remove(n)
        num[0] += 1
    while 'W' in S:
        for n in nums[2]:
            S.remove(n)
        num[2] += 1
    while 'U' in S:
        for n in nums[4]:
            S.remove(n)
        num[4] += 1
    while 'X' in S:
        for n in nums[6]:
            S.remove(n)
        num[6] += 1
    while 'G' in S:
        for n in nums[8]:
            S.remove(n)
        num[8] += 1
    while 'S' in S:
        for n in nums[7]:
            S.remove(n)
        num[7] += 1
    while 'V' in S:
        for n in nums[5]:
            S.remove(n)
        num[5] += 1
    while 'R' in S:
        for n in nums[3]:
            S.remove(n)
        num[3] += 1
    while 'O' in S:
        for n in nums[1]:
            S.remove(n)
        num[1] += 1
    while 'N' in S:
        for n in nums[9]:
            S.remove(n)
        num[9] += 1
    print('Case #', i, ':', sep='', end=' ')
    for i in range(10):
        print(str(i) * num[i], end='')
    print()