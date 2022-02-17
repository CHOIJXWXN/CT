N = int(input())
unordered = []
for i in range(N):
    unordered.append(int(input()))
print(*sorted(unordered), sep = '\n')