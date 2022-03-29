'''
내일 할거야
'''
import sys

n = int(sys.stdin.readline().rstrip())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
A.sort(key=lambda x: -x[1])
for i in range(n - 1):
    if A[i][1] - A[i][0] + 1 <= A[i + 1][1]:
        A[i + 1][1] = A[i][1] - A[i][0]
print(A[-1][1] - A[-1][0])