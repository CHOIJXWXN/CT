'''

'''
N = int(input())
w = list()
for _ in range(N):
    w.append(int(input()))
w.sort()
max_w = 0
for i in range(N):
    max_w = max(max_w, w[-1 -i] * (i + 1))
print(max_w)