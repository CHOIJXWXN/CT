'''
3의 배수
a + b + c = N
3HN = (N + 2)C2
'''
n = int(input())
n = n // 3 - 3
print((n + 2) * (n + 1)//2)