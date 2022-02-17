N = int(input())
unrank = []
rank = []
for i in range(N):
    person = list(map(int, input().split()))
    unrank.append(person)
for i in range(N):
    cnt = 1
    for j in range(N):
        if unrank[i][0] < unrank[j][0] and unrank[i][1] < unrank[j][1]:
            cnt += 1
    rank.append(cnt)
print(*rank)