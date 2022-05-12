'''
자연수 색칠하기
소수면 새로운 색깔
'''
N = int(input())
color = [1] * N
idx = 1
for i in range(2, N + 1):
    if color[i - 1] == 1:
        idx += 1
        for j in range(N // i):
            color[i * (j + 1) - 1] = idx
print(idx)
print(*color)
