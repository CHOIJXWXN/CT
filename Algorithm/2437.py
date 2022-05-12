'''
저울
'''
import sys

N = int(input())
num = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
sum = 1
for i in range(N):
    if sum < num[i]:
        break
    sum += num[i]
print(sum)