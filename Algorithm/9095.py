'''
1, 2, 3 더하기
'''
import sys

read = sys.stdin.readline
T = int(read())
A = [0, 1, 2, 4]
input = list()
for _ in range(T):
    input.append(int(read()))
max_input = max(input)
for i in range(4, max_input + 1):
    A.append((A[-1] + A[-2] + A[-3]) % 1000000009)
for i in input:
    print(A[i])