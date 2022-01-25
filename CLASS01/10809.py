S = input()
results = [-1] * 26
for i in range(len(S)):
    if results[ord(S[i]) - 97] == -1:
        results[ord(S[i]) - 97] = i
print(*results)