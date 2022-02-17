N = int(input())
generator = 0
if N < 10000:
    i = N // 2
else:
    i = int(N * 0.9)
while not generator:
    for num in str(i):
        decompose = sum([int(num) for num in str(i)]) + i
        if decompose == N:
            generator = i
    i += 1
    if i > N:
        break
print(generator)

# 이거 좀 어거지인데...
