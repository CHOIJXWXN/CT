'''
나무 자르기
그리디
'''
# n = int(input())
# trees = list(map(int, input().split()))
# d = list(map(int, input().split()))
# for i in range(n):
#     trees[i] += d[i]
# tot = 0
# for _ in range(n):
#     m = max(trees)
#     tot += m
#     for i in range(n):
#         if trees[i] == m:
#             trees[i] = 0
#         trees[i] += d[i]
# print(tot)

n = int(input())
tot = 0
trees = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
trees.sort(key=lambda x:x[1])
for i in range(n):
    tot += trees[i][0] + i * trees[i][1]
print(tot)