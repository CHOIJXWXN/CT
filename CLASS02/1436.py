N = int(input())
n = 666
cnt = 1
while cnt < N:
    n += 1
    if str(n).count('666'):
        cnt += 1
print(n)