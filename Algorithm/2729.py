'''
이진수 덧셈
'''
T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    print(bin(int('0b' + a, 2) + int('0b' + b, 2))[2:])