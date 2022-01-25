max_num = 0
idx = 0
for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        idx = i + 1

print(max_num)
print(idx)