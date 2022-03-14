'''
2로 몇 번 나누어질까
'''
# A, B = map(int, input().split())
# tot = 0
# for i in range(A, B + 1):
#     tot += 1<<len(bin(i).split('1')[-1])
# print(tot)

# A, B = map(int, input().split())
# tot = 0
# for i in range(A, B + 1):
#     n = 1
#     while not i % 2:
#         n *= 2
#         i //= 2
#     tot += n
# print(tot)

A, B = map(int, input().split())
tot = B - (A - 1)                       # 범위 내 1 더하기
i = 2
while i <= B:
    tot += (B // i) * (i // 2)          # 1 ~ B까지 범위 내 2, 4, 8, ... 배수의 개수만큼 더하기
    i *= 2
i = 2
while i <= A - 1:
    tot -= ((A - 1) // i) * (i // 2)    # 1 ~ A - 1까지 범위 2, 4, 8, ... 배수의 개수만큼 빼기
    i *= 2
print(tot)