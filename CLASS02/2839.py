N = int(input())
q = N // 5
r = N % 5
p = [0, 2, 4, 1, 3]
d = [0, -1, -2, 0, -1]
print('-1') if q + d[r] < 0 else print(q + d[r] + p[r])