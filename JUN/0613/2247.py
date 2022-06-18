"""
실질적 약수
"""

N = int(input())
csod = 0
for i in range(2, N // 2 + 1):
    csod += (N // i - 1) * i
print(csod % 1000000)

"""
CSOD 13
SOD 1       0
SOD 2       0
SOD 3       0
SOD 4       2
SOD 5       0
SOD 6       5
SOD 7       0
SOD 8       6
SOD 9       3
SOD 10      7
SOD 11      0
SOD 12      15
SOD 13      0

CSOD 13     38

2의 배수 : 6개 - 1개 = 5개    10
3의 배수 : 4개 - 1개 = 3개    9
4의 배수 : 3개 - 1개 = 2개    8
5의 배수 : 2개 - 1개 = 1개    5
6의 배수 : 2개 - 1개 = 1개    6
                          38
"""
