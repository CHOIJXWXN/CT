'''
돌 게임
N = 1일 때, SK
N = 2일 때, 2 -> 1, CY
N = 3일 때, SK
N = 4일 때, 4 -> 1, CY 혹은 4 -> 3, CY
N = 5일 때, 5 -> 4, SK 혹은 5 -> 2, SK
즉, 홀수이면 SK가 이기고 짝수이면 CY가 이김
'''
N = int(input())
print('SK') if N % 2 else print('CY')